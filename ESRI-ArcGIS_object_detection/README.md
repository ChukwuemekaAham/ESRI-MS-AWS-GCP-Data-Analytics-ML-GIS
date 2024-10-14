## Object Detection for Swimming Pool Identification Using ArcGIS Pro

This project uses ArcGIS Pro's deep learning capabilities to detect swimming pools within an aerial imagery dataset. This project addresses a common challenge faced by tax assessors at local government agencies - ensuring accurate property value estimations and tax calculations. 

**Scenario:**

Tax assessors often rely on infrequent surveys to estimate property values.  Swimming pools significantly impact property value, but these surveys may miss newly constructed pools. This project aims to address this challenge by using ArcGIS deep learning tools to automatically detect all swimming pools in a defined area. Tax assessors can use this information to identify unrecorded pools, leading to more accurate property assessments and potential additional revenue for the community.

**1. Data Preparation:**

* Download the necessary data files 

**2. Verify ArcGIS Pro License and Extensions:**

* Open ArcGIS Pro and go to Settings -> Licensing.
* Ensure you have access to the Advanced ArcGIS Pro Named User License and the Image Analyst extension.

**3. Open the Project:**

* Open the `ObjectDetection.aprx` project from the `ObjectDetection` folder. The imagery file shows a false-color image of an area in Southern California. This false-color image uses an infrared band to visualize vegetation in red. Although one can use a true-color image for this analysis, the false-color image better distinguishes pools from other objects.

![Screenshot 2023-10-01 162747.png](./screenshot/Screenshot%202023-10-01%20162747.png)

**4. Create Training Samples:**

The first step in object detection was to prepare training data that will be used to train the model. There are various ways to
prepare training samples:
- Use ArcGIS Pro editing tools.
- Use the Label Objects For Deep Learning tool.
- Use crowdsourced data (for example, community-based damage assessments).
- Use preexisting data as training samples (for example, a feature class of building footprints).

* The training samples was prepared by using the `Label Objects For Deep Learning tool`

I selected the `NAIP_AOI.tif` imagery file, navigate to the Classification Tools under the Imagery tab, and used the Polygon tool to outline the swimming pools in Pool 1 and Pool 2 bookmarks, labeling them as "Pool" with a Class Value of "0" in the Define Class dialog box.

![Screenshot 2023-10-01 162747.png](./screenshot/Screenshot%202023-10-01%20162747.png)

**5. Review Training Samples:**

* Adding the `TrainingSamplesComplete` feature class to the map and visualizing the pre-created training samples.
* From the attribute table we can confirm that the `ClassValue` field contains the value "0".

![Screenshot 2023-10-01 191710.png](./screenshot/Screenshot%202023-10-01%20191710.png)

**6. Export Training Samples to Image Chips:**

After creating the training samples, `Export Training Data For Deep Learning (Image Analyst Tools)` tool was used to export these training samples into a `TIFF` that can be used to train the model.

![Screenshot 2023-10-01 191927.png](./screenshot/Screenshot%202023-10-01%20191927.png)

![Screenshot 2023-10-01 193243.png](./screenshot/Screenshot%202023-10-01%20193243.png)

* parameters:
    * Input Raster: `NAIP_AOI.tif`
    * Output Folder: `ImageChips`
    * Input Feature Class: `TrainingSamplesComplete`
    * Class Value Field: `ClassValue`
    * Buffer Radius: 6 meters (to capture the pool shapes)
    * Remaining parameters set at their default values.

**7. Review Image Chips:**

The tool creates a folder for the image chips that includes the images, label definitions for the images, image statistics, and a
model definition file. The `model definition file` references this image chip information, and will be used to train the model

* Open the `ImageChips` folder in the `ObjectDetection` directory.
* Browse the `Images` folder and open one of the TIF files to see an example of an image chip used for model training.

![Screenshot 2023-10-01 193840.png](./screenshot/Screenshot%202023-10-01%20193840.png)


## Train and Use an Object Detection Model for Swimming Pools in ArcGIS Pro

This part, demonstrates training and using a deep learning model to detect swimming pools in a defined area. 

**1. Verify Deep Learning Libraries:**

* Open the Python Command Prompt from the Windows Start menu.
* Type `conda list` and press Enter.
* Locate the `deep-learning-essentials` package in the list. Ensure the version matches your installed ArcGIS Pro version (3.1 in this case).
* **If necessary, uninstall the old version of the `deep-learning-essentials` package and install the newer version.**
* **If you don't have the `deep-learning-essentials` package, follow the instructions at `Install deep learning frameworks for ArcGIS` (`https://links.esri.com/InstallDeepLearning`) and restart ArcGIS Pro.**

**2. Train the Model Using Geoprocessing Tools:**

* Open the `ObjectDetection.aprx` project from the `ObjectDetection` folder.
* The `Train Deep Learning Model (Image Analyst Tools)` tool was used to train the model using the following parameters:
    * Input Training Data: `ImageChips` folder.
    * Output Model: `PoolsModel_25_SSD`.
    * Max Epochs: `25` (You can adjust this based on your model's performance).
    * Model Type: `Single Shot Detector (Object Detection)`.

    The model type will determine the deep learning algorithm and neural network that you will use to
    train your model. The models that are available to you depend on the metadata format that is
    chosen for the image chips. You chose a metadata format that is associated with object detection,
    so only the object detection model types are available. For more information about the other model types, go to ArcGIS Pro Help: Train Deep Learning Model (Image Analyst).

    * **Optional: Adjust the `Model Arguments` (grid cell size, zoom level, aspect ratio) and `Advanced` settings based on your needs and preferences.**

    Model arguments refer to specific parameter values that are used to train the model. The model
    arguments will vary based on the model type that you choose. For the Single Shot Detector (Object
    Detection) model type, you can specify the grid cell size, zoom level, and aspect ratio. These values
    define how the model examines the image to detect objects. For more information about the
    Single Shot Detector model, go to ArcGIS API for Python Help: How single-shot detector (SSD)
    works.
    
    To learn more about the individual model parameters, point to Model Arguments and pause on the
    geoprocessing input information icon

* **Note: Training this model can take up to four hours.**

**3. Reviewing the Model:**

* Open File Explorer and browse to `..\ObjectDetection\Results\PoolsModel_25_SSD`.

* Double-click the `model_metrics.html` file.

* `Learning rate` controls the speed at which the model is trained, which shows how quickly the
model parameters are updated. In this graphic, the learning rate shows a range of values, where
the smaller number on the left is the learning rate applied to the first few layers of the network,
and the larger number on the right is applied to the last few layers. The low learning rate trains
the first few layers of the network slowly while the higher learning rate trains the final layers of
the network more quickly. The end goal is to identify your optimal learning rate. That can be
done by finding the highest learning rate where the loss is still improving; since loss is an
indicator of error, a smaller number is more ideal.

* `The training and validation loss graph` compares training and validation losses over the
training epochs. A model that performs well typically shows a continual decrease in both
training and validation loss over the training epochs. If the validation loss begins to increase,
then you may have overfitting, where the model is recognizing a particular set of data too
closely and therefore may not generalize well to other data.

* `Average precision score` assesses the performance of object detection models. It measures
the average precision for the validation set for each class. An average precision score ranges
from 0 to 1, where values closer to 1 indicate better model performance

* `Ground truth`

Comparing the ground truth images with the predicted images also help to determine the accuracy of the model. This model provides a good baseline, predicting most of the pools identified in the ground truth image.

These metrics can help to determine whether should modify the parameters of this tool (learning rate, number of epochs, grid cell size, and so on) to improve the results of the models.

**4. Perform Inferencing using the Model:**

Inferencing uses the trained model to extract information from the imagery. In this case, extract, or detect, swimming pools for
the specified area of interest.

* Using the `Detect Objects Using Deep Learning (Image Analyst Tools)` tool.
* Parameters:
    * Input Raster: `NAIP_AOI.tif`.
    * Output Detected Objects: `SwimmingPoolsAll`.
    * Model Definition: Browsed to `..\EsriTraining\ObjectDetection\Results\PoolsModel_25_SSD` and selected `PoolsModel_25_SSD.emd`.
    * **You can adjust the `Arguments` and `Advanced` settings based on your analysis requirements**

    The following information provides explanations of each argument:

    - Padding adds a border of cells around the image. This border is used to ensure that the image
    maintains its original size as it passes through the model. Padding is most relevant if you are
    detecting objects that are around the edge of your image.

    - Threshold defines the required confidence level for object detection. In this analysis, the
    threshold is 0.5, meaning that the model has to be at least 50 percent confident that the object
    is a swimming pool.

    - NMS_Overlap is the percentage of allowable overlap between features. In this analysis,
    features that overlap more than 10 percent will be removed.

    - Batch_Size should be a square number, such as 1, 4, 9, 16, and so on. If the input value is not a
    perfect square, the analysis will use the largest perfect square that is less than the input.
    Increasing the batch size can improve tool performance. However, as the batch size increases,
    more memory is used.

    - Exclude_Pad_Detections allows you to exclude items in the padded areas. In this analysis, you
    will exclude the padded areas from inferencing.


    * Checked the `Non Maximum Suppression` box.

**5. Review Inferencing Results:**

* **Visually, assessing the accuracy of the model's predictions**

![Screenshot 2023-10-01 193744.png](./screenshot/Screenshot%202023-10-01%20193744.png)

**6. Train The Model with ArcGIS API for Python:**

* **Follow the steps in the `model_training.ipynb` Jupyter Notebook to train the model using ArcGIS API for Python.**
* **Note: The training process can take up to four hours. The notebook includes detailed instructions for each step.**

**7. Conclusion:**

Using this model, we can quickly detect the remaining swimming pools in Southern California, providing tax assessors with the information that they need to identify more accurate property values and taxes