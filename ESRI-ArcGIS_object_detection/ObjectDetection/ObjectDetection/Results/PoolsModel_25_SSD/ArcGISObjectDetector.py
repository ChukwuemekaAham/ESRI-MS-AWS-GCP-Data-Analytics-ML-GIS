
import json
import sys, os, importlib
sys.path.append(os.path.dirname(__file__))

import numpy as np
import math
import arcpy

def check_centroid_in_center(centroid, start_x, start_y, chip_sz, padding):
    return ((centroid[1] >= (start_y + padding)) and                  (centroid[1] <= (start_y + (chip_sz - padding))) and                 (centroid[0] >= (start_x + padding)) and                 (centroid[0] <= (start_x + (chip_sz - padding))))

def find_i_j(centroid, n_rows, n_cols, chip_sz, padding, filter_detections):
    for i in range(n_rows):
        for j in range(n_cols):
            start_x = i * chip_sz
            start_y = j * chip_sz

            if (centroid[1] > (start_y)) and (centroid[1] < (start_y + (chip_sz))) and (centroid[0] > (start_x)) and (centroid[0] < (start_x + (chip_sz))):
                in_center = check_centroid_in_center(centroid, start_x, start_y, chip_sz, padding)
                if filter_detections:
                    if in_center: 
                        return i, j, in_center
                else:
                    return i, j, in_center
    return None


def get_available_device(max_memory=0.8):
    '''
    select available device based on the memory utilization status of the device
    :param max_memory: the maximum memory utilization ratio that is considered available
    :return: GPU id that is available, -1 means no GPU is available/uses CPU, if GPUtil package is not installed, will
    return 0 
    '''
    try:
        import GPUtil
    except ModuleNotFoundError:
        return 0

    GPUs = GPUtil.getGPUs()
    freeMemory = 0
    available=-1
    for GPU in GPUs:
        if GPU.memoryUtil > max_memory:
            continue
        if GPU.memoryFree >= freeMemory:
            freeMemory = GPU.memoryFree
            available = GPU.id

    return available

features = {
    'displayFieldName': '',
    'fieldAliases': {
        'FID': 'FID',
        'Class': 'Class',
        'Confidence': 'Confidence'
    },
    'geometryType': 'esriGeometryPolygon',
    'fields': [
        {
            'name': 'FID',
            'type': 'esriFieldTypeOID',
            'alias': 'FID'
        },        
        {
            'name': 'Class',
            'type': 'esriFieldTypeString',
            'alias': 'Class'
        },
        {
            'name': 'Confidence',
            'type': 'esriFieldTypeDouble',
            'alias': 'Confidence'
        }
    ],
    'features': []
}

fields = {
    'fields': [
        {
            'name': 'OID',
            'type': 'esriFieldTypeOID',
            'alias': 'OID'
        },      
        {
            'name': 'Class',
            'type': 'esriFieldTypeString',
            'alias': 'Class'
        },
        {
            'name': 'Confidence',
            'type': 'esriFieldTypeDouble',
            'alias': 'Confidence'
        },
        {
            'name': 'Shape',
            'type': 'esriFieldTypeGeometry',
            'alias': 'Shape'
        }
    ]
}

class GeometryType:
    Point = 1
    Multipoint = 2
    Polyline = 3
    Polygon = 4


class ArcGISObjectDetector:
    def __init__(self):
        self.name = 'Object Detector'
        self.description = 'This python raster function applies deep learning model to detect objects in imagery'

    def initialize(self, **kwargs):
        if 'model' not in kwargs:
            return

        model = kwargs['model']
        model_as_file = True
        try:
            with open(model, 'r') as f:
                self.json_info = json.load(f)
        except FileNotFoundError:
            try:
                self.json_info = json.loads(model)
                model_as_file = False
            except json.decoder.JSONDecodeError:
                raise Exception("Invalid model argument")

        sys.path.append(os.path.dirname(__file__))
        framework = self.json_info['Framework']
        if 'ModelConfiguration' in self.json_info:
            if isinstance(self.json_info['ModelConfiguration'], str):
                ChildModelDetector = getattr(importlib.import_module(
                    '{}.{}'.format(framework, self.json_info['ModelConfiguration'])), 'ChildObjectDetector')
            else:
                ChildModelDetector = getattr(importlib.import_module(
                    '{}.{}'.format(framework, self.json_info['ModelConfiguration']['Name'])), 'ChildObjectDetector')
        else:
            raise Exception("Invalid model configuration")

        device = None
        if 'device' in kwargs:
            device = kwargs['device']
            if device == -2:
                device = get_available_device()

        if device is not None:
            if device >= 0:
                os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
                os.environ['CUDA_VISIBLE_DEVICES'] = str(device)
                arcpy.env.processorType = "GPU"
                arcpy.env.gpuId = str(device)
            else:
                arcpy.env.processorType = "CPU"

        self.child_object_detector = ChildModelDetector()
        self.child_object_detector.initialize(model, model_as_file)

    def getParameterInfo(self):
        required_parameters = [
            {
                'name': 'raster',
                'dataType': 'raster',
                'required': True,
                'displayName': 'Raster',
                'description': 'Input Raster'
            },
            {
                'name': 'model',
                'dataType': 'string',
                'required': True,
                'displayName': 'Input Model Definition (EMD) File',
                'description': 'Input model definition (EMD) JSON file'
            },
            {
                'name': 'device',
                'dataType': 'numeric',
                'required': False,
                'displayName': 'Device ID',
                'description': 'Device ID'
            }
        ]
        return self.child_object_detector.getParameterInfo(required_parameters)

    def getConfiguration(self, **scalars):
        configuration = self.child_object_detector.getConfiguration(**scalars)
        if 'DataRange' in self.json_info:
            configuration['dataRange'] = tuple(self.json_info['DataRange'])
        configuration['inheritProperties'] = 2|4|8
        configuration['inputMask'] = True
        return configuration

    def getFields(self):
        return json.dumps(fields)

    def getGeometryType(self):
        return GeometryType.Polygon

    def vectorize(self, **pixelBlocks):
        # set pixel values in invalid areas to 0
        raster_mask = pixelBlocks['raster_mask']
        raster_pixels = pixelBlocks['raster_pixels']
        raster_pixels[np.where(raster_mask == 0)] = 0
        pixelBlocks['raster_pixels'] = raster_pixels

        polygon_list, scores, classes = self.child_object_detector.vectorize(**pixelBlocks)

        n_rows = int(math.sqrt(self.child_object_detector.batch_size))
        n_cols = int(math.sqrt(self.child_object_detector.batch_size))
        padding = self.child_object_detector.padding
        keep_polygon = []
        keep_scores = []
        keep_classes = []

        for idx, polygon in enumerate(polygon_list):
            centroid = polygon.mean(0)
            quadrant = find_i_j(centroid, n_rows, n_cols, self.json_info['ImageHeight'], padding, self.child_object_detector.filter_outer_padding_detections)        
            if quadrant is not None:
                i, j, in_center = quadrant             
                polygon[:, 0] = polygon[:, 0] - (2*i + 1)*padding
                polygon[:, 1] = polygon[:, 1] - (2*j + 1)*padding
                keep_polygon.append(polygon)
                if not in_center:
                    scores[idx] = (self.child_object_detector.thres * 100) + scores[idx] * 0.01
                keep_scores.append(scores[idx])
                keep_classes.append(classes[idx])

        polygon_list =  keep_polygon
        scores = keep_scores
        classes = keep_classes
        features['features'] = []
        for i in range(len(polygon_list)):
            rings = [[]]
            for j in range(polygon_list[i].shape[0]):
                rings[0].append(
                    [
                        polygon_list[i][j][1],
                        polygon_list[i][j][0]
                    ]
                )

            features['features'].append({
                'attributes': {
                    'OID': i + 1,                
                    'Class': self.json_info['Classes'][classes[i] - 1]['Name'],
                    'Confidence': scores[i]
                },
                'geometry': {
                    'rings': rings
                }
            })   
            
        return {'output_vectors': json.dumps(features)}

