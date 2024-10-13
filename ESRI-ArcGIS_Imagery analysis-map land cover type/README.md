# Water Policy Assessment in Paradise Valley, Arizona

**Introduction:**

Imagery in serves multiple purposes, from providing context for location-based studies to being the focal point for new discoveries or quantifying study area aspects. A critical first step in using remote sensing data is examining the imagery dataset itself, as the ability to identify features is linked to the dataset's characteristics, which vary by sensor type. Metadata associated with imagery includes essential details such as collection date, spatial reference, and area, which enhance feature discovery.

Understanding technical aspects of imagery improves the ability to find desired features, as remote sensing data captures information in raster bands. Each raster band records specific characteristics, and datasets can contain multiple bands that can be combined or displayed as composites based on visualization needs.

Imagery analysis in ArcGIS Pro offers advanced capabilities that surpass those of imagery web apps, allowing users to work with diverse data sources, including dynamic image services from the Landsat Viewer and layers from the ArcGIS Living Atlas of the World. 

Spatial resolution is very important during imagery analysis, as higher resolution imagery enables better discernibility of features, leading to more refined analysis results.

**Part One:**

**Using Imagery to Locate Areas of Interest: Identifying Areas of High Vegetation**

In this part of the project, I explored Landsat imagery using the ArcGIS Landsat Explorer app to locate areas with high vegetation. This knowledge will be used to identify areas that may be most affected by changes in water policy.

![water policy](./Locate%20areas%20of%20interest/Screenshot%202023-09-28%20132845.png)

The Landsat sensor's spectral bands are reported as raster bands when viewed in ArcGIS apps. There is a raster band for each
spectral band collected by the satellite


**Scenario:**

As a GIS analyst working for a local government, I am tasked with assessing the potential impact of revisions to the water policy.  To identify businesses most affected by these changes, I need to locate areas with the most significant amount of vegetation, which require substantial irrigation.  I used the Landsat Explorer app to explore satellite imagery and find areas with high vegetation index values.


**1. Reporting Spectral Information:**

The Landsat 9 sensor collects 11 spectral bands. For more information about the specific wavelengths collected, visit the USGS
website for the Landsat 9 sensor (https://links.esri.com/USGSLandsat9 | https://www.usgs.gov/landsat-missions/landsat-9).

![water policy](./Locate%20areas%20of%20interest/Screenshot%202024-10-08%20163615.png)

The spectral information is reported as raster bands

**Multispectral bands for Landsat 8 and 9**
| Band | Description                     |
|------|---------------------------------|
| 1    | Coastal Aerosol                |
| 2    | Blue                            |
| 3    | Green                           |
| 4    | Red                             |
| 5    | Near Infrared                  |
| 6    | Shortwave Infrared 1           |
| 7    | Shortwave Infrared 2           |
| 8    | Panchromatic                    |
| 9    | Cirrus                          |
| 10   | Thermal Infrared Sensor 1      |
| 11   | Thermal Infrared Sensor 2      |


![water policy](./Locate%20areas%20of%20interest/Screenshot%202024-10-08%20163410.png)


Imagery is displayed in a combination of three bands. Which three bands are displayed depends on the chosen rendering.

The rendering options for each Landsat image depend on the metadata, which provides information on which of the 11 total
bands are present in the product. 

Esri provides a series of Landsat image layers as dynamic imagery layers. Preconfigured visualizations from the Landsat raster bands are available with the layers. These custom visualizations are called renderers


**2. Visualizing the study area and creating a vegetation index, mask and vegetation study area layer**

I logged into my ArcGIS Online account and accessed the Landsat Explorer web app to explore Landsat imagery. Through this app, I learned about the Landsat program and its sensors, identifying the current renderer and the specific spectral bands used for visualization. I adjusted the visualization to minimize cloud cover and changed the renderer to display healthy vegetation in shades of red.

* Landsat Explorer web app: [https://links.esri.com/LandsatExplorer](https://links.esri.com/LandsatExplorer).

* **Visualize the study area and  add a study area layer to the map.**

![water policy](./Locate%20areas%20of%20interest/Screenshot%202023-09-28%20112957.png)

Zoomed into `Paradise Valley, AZ`, and identified visible vegetation features, noting their association with parks and golf courses, `McCormick Ranch Golf Club` slightly northeast of Paradise Valley. After adding a study area layer, I created a Vegetation Index to highlight areas of vegetation in green, visually confirming their locations against the underlying basemap.

`Potential Area for Water Policy`

![water policy](./Locate%20areas%20of%20interest/Screenshot%202023-09-28%20114321.png)


* **Vegetation Index**

The Vegetation Index is based on the `Normalized Difference Vegetation Index (NDVI)` and is used to measure and monitor
vegetation health. It uses the `Near Infrared` and `Red` raster bands and is calculated with the following formula:

* **(Near Infrared - Red) / (Near Infrared + Red)**

![water policy](./Locate%20areas%20of%20interest/Screenshot%202023-09-28%20115733.png)


The Near Infrared band is vital in identifying and monitoring vegetation. The values in this index are listed on a scale
range from -1.0 to 1.0. The greater values (green) indicate the presence of rich vegetation in the area.

![water policy](./Locate%20areas%20of%20interest/Screenshot%202023-09-28%20122036.png)

As previously identified, the green areas in the Vegetation Index appear to correlate to the golf courses and parks.

* **Vegetation Mask**

Next, I created a `Vegetation Mask` by defining `Areas of Interest` within the study area, adjusting the mask value to highlight high vegetation areas in `Blue`. 

A`local expert` has determined that a value of `0.45` is appropriate. The values for the mask cover the vegetation areas in the study area well.

![water policy](./Locate%20areas%20of%20interest/Screenshot%202023-09-28%20133021.png)

`NDVI Mask For Water Policy [initials]` saved with relevant tags, successfully representing areas of high vegetation within my study area.

* **Vegetation study area layer**

![water policy](./Locate%20areas%20of%20interest/Screenshot%202023-09-28%20134756.png)


*******************************************************************

## Accessing satellite data in ArcGIS Pro

**Part Two:**

In this phase of my research on water policy impacts around `Paradise Valley, Arizona`, I utilized ArcGIS Pro to compare vegetation areas using both `Landsat` and `Sentinel-2` imagery layers. I began by adding my previously created `NDVI Mask layer` to Map Viewer. Created a new project named `WaterImpactPolicy` and added relevant layers, including the `Potential Area for Water Policy` and my `NDVI Mask layer`, while adjusting their symbology for better visualization.


![water policy](./screenshot/Screenshot%202023-09-29%20132724.png)

Continuing my analysis, I examined the `Landsat GLS Multispectral` layer's properties. 

![water policy](./screenshot/Screenshot%202023-09-29%20133412.png)

The Agriculture band combination of 5,4,1 is being used by default, three bands are reported. The imagery layer contains all the raster bands for the Landsat image, but it only returns the specific raster bands based on the selected processing template.

![water policy](./screenshot/Screenshot%202023-09-29%20134434.png)

`cell size`

![water policy](./screenshot/Screenshot%202023-09-29%20140330.png)

![water policy](./screenshot/Screenshot%202023-09-29%20140401.png)


Spatial resolution can be considered high to low or coarse to fine. When the cell size number is small, the raster is considered to have a high spatial resolution.


Added the higher-resolution `Sentinel-2` imagery layer for comparison. The Sentinel-2 Views imagery layer displays in Natural Color by default.

![water policy](./screenshot/Screenshot%202023-09-29%20142916.png)

`cell size`

![water policy](./screenshot/Screenshot%202023-09-29%20143147.png)

The Sentinel-2 Views imagery layer is based on imagery data collected by the Sentinel-2 satellite. The Sentinel-2 satellite carries
an optical instrument payload that samples 13 spectral bands: four bands at 10-meter, six bands at 20-meter, and three bands at
60-meter spatial resolutions. This imagery layer pulls directly from the Sentinel-2 on the Amazon Web Services collection and is
updated daily with new imagery.

For more information about the Sentinel-2 Views imagery layer, review the item page on ArcGIS Online (https://links.esri.com/Sentinel-2 | https://arcgis.com/home/item.html?id=fd61b9e0c69c4e14bebd50a9a968348c)


I modified processing templates for both layers to `NDVI Raw` and adjusted the `NDVI Mask` layer's transparency to enhance my analysis.

By employing the Swipe tool, I visually assessed differences in spatial resolution between the two datasets, noting how the sharper Sentinel imagery revealed finer details in vegetation areas, Landsat imagery layer has a lower spatial resolution,
features are not as well-defined, meaning that certain areas of high vegetation may be missed. With the higher resolution
Sentinel imagery layer features are more defined and smaller areas of high vegetation are more likely to be detected. 

Through these steps, I effectively compared the two imagery sources to evaluate their impacts on identifying vegetation in the study area, preparing for further analysis in subsequent exercises.

****************************************************************

##  Using satellite data to map the land cover type

**Part Three:**

This part focuses on using the higher-resolution Sentinel-2 imagery layer with similar multispectral characteristics, created with ArcGIS Image for ArcGIS Online, to refine the vegetation analysis in ArcGIS Pro to obtain more accurate measurements of the vegetation areas after reviewing the vegetation mask based on Landsat imagery,

![water policy](./screenshot%202/Screenshot%202023-09-30%20132233.png)

`Sentinel-2 raster bands`
| Band | Description                       | Spatial Resolution (meters) |
|------|-----------------------------------|------------------------------|
| 1    | Coastal Aerosol                  | 60                           |
| 2    | Blue                              | 10                           |
| 3    | Green                             | 10                           |
| 4    | Red                               | 10                           |
| 5    | Vegetation Red Edge              | 20                           |
| 6    | Vegetation Red Edge              | 20                           |
| 7    | Vegetation Red Edge              | 20                           |
| 8    | Near Infrared                    | 10                           |
| 8a   | Narrow Near Infrared             | 20                           |
| 9    | Water Vapor                      | 60                           |
| 10   | Shortwave Infra

In the `WaterImpactPolicy` project within ArcGIS Pro, I began by renaming the current map to "Preliminary Study" and added the `Paradise Valley Multispectral` tiled imagery layer, derived from Sentinel-2 data. 

![water policy](./screenshot%202/Screenshot%202023-09-30%20132233.png)

![water policy](./screenshot%202/Screenshot%202023-09-30%20132616.png)

The Sentinel imagery that was added to the map has been created for the vegetation analysis using only the high-resolution bands (Red, Green, Blue, Near Infrared)

![water policy](./screenshot%202/Screenshot%202023-09-30%20132811.png)

![water policy](./screenshot%202/Screenshot%202023-09-30%20132845.png)

![water policy](./screenshot%202/Screenshot%202023-09-30%20132856.png)

The Paradise Valley Multispectral imagery layer was created in ArcGIS Image for ArcGIS Online with
the Multispectral-10m template. The template determines which bands are added to the imagery
layer and the default visualization. Each configuration option during the publishing affects the bands
that are used for the imagery layer, which can affect the spatial resolution of the imagery layer.

After reviewing the layer's properties and metadata, I incorporated additional layers, including the `Potential Area For Water Policy` and my `NDVI Mask For Water Policy`. 

![water policy](./screenshot%202/Screenshot%202023-09-30%20134318.png)

![water policy](./screenshot%202/Screenshot%202023-09-30%20134737.png)

I changed the Sentinel imagery rendering to `Color Infrared`, applying `Dynamic Range Adjustment (DRA)` to enhance vegetation visibility. This setup allowed me to effectively focus on the study area while preparing for further analysis.

![water policy](./screenshot%202/Screenshot%202023-09-30%20135225.png)

Next, I processed the Sentinel imagery to create a vegetation index using `NDVI calculations`, enabling a visual representation of vegetation density. In ArcGIS Pro, you can analyze imagery using geoprocessing tools or raster functions. There are
benefits to each processing method, and both can be used separately or together. 

| Processing Method     | Benefits                                                                                       |
|-----------------------|------------------------------------------------------------------------------------------------|
| Geoprocessing Tool    | - Creates new data on disk                                                                     |
|                       | - Easily view and edit geoprocessing history                                                    |
|                       | - Create and use custom geoprocessing tools                                                    |
|                       | - Use batch geoprocessing                                                                      |
|                       | - String together processes for complex modeling                                                |
|                       | - Save sets of geoprocessing tools in your project                                             |
|                       | - Can be run in the Enterprise environment to use distributed processing                        |
| Raster Function       | - No new dataset created                                                                         |
|                       | - Fast and efficient; on the fly                                                                |
|                       | - Easily view and edit raster function history                                                   |
|                       | - Create and use custom raster functions                                                         |
|                       | - Chain together processes for complex modeling                                                 |
|                       | - Save sets of raster functions in your project                                                 |
|                       | - Generate processing templates for image services                                              |
|                       | - Can be run in the Enterprise environment to use distributed processing                         |


The primary
difference between the two is that with `raster functions`, calculations are applied directly to the pixels
viewed in the display. This means that as we zoom and pan around the display, the calculations will
quickly and efficiently update what is seen on the display.

* Selected the `Paradise Valley Multispectral` imagery layer.
* From the `Imagery` tab, I clicked `Indices` -> `NDVI`.
* Set the following parameters:
    * Near Infrared Band Index: `4 - B8`
    * Red Band Index: `3 - B4`

![water policy](./screenshot%202/Screenshot%202023-09-30%20140032.png)

The values are `1 to -0.4229` are reported in the `NDVI_Paradise Valley Multispectral` layer

![water policy](./screenshot%202/Screenshot%202023-09-30%20141042.png)


The `Band Arithmetic Properties` -> formula used to calculate the NDVI: 

`(NIR - Red) / (NIR + Red)`

![water policy](./screenshot%202/Screenshot%202023-09-30%20141258.png)

**Focusing the Analysis Results:**

I clipped this index to my study area, generating a new layer that highlighted regions with NDVI values exceeding 0.45.

* `Raster Functions` -> `Clip` function properties.
* Parameters:
    * Raster: `NDVI_Paradise Valley Multispectral`.
    * Clipping Geometry/Raster: `WaterPolicyStudyArea`.
    * Checked the box for `Use Input Features For Clipping Geometry`.
* Created a new layer.

![water policy](./screenshot%202/Screenshot%202023-09-30%20142442.png)

**Outcome:** A new layer named `Clip_NDVI_Paradise Valley Multispectral` was created, clipping the NDVI layer to the study area.

**Creating a New Mask:**

Refined vegetation mask

* `Raster Functions` -> `Greater than` function properties.
* Parameters:
    * Raster: `Clip_NDVI_Paradise Valley Multispectral`
    * Raster2: `0.45` (This will create a constant raster with a value of 0.45)
    * Cellsize Type: `Max Of`
    * Extent Of: `Intersection Of`
* Created a new layer. 

**Outcome:** A new layer named `Greater_Than_Clip_NDVI_Paradise Valley Multispectral` was created, highlighting areas where the NDVI value exceeds 0.45 (representing high vegetation density).

![water policy](./screenshot%202/Screenshot%202023-09-30%20144032.png)

Changed the `Primary Symbology` of `Greater_Than_Clip_NDVI_Paradise Valley Multispectral` from `Stretch` to `Classify`, with values greater than 0.45 displayed as "1" and values less than 0.45 displayed as "0". 

* Changed the `Symbology` - color swatch for the "0" value to `No Color` and the "1" value to a `green color`.

![water policy](./screenshot%202/Screenshot%202023-09-30%20144717.png)


**6. Review the Area Calculation:**

Comparing the vegetation mask created from the Sentinel imagery to the
mask created from the Landsat imagery

![water policy](./screenshot%202/Screenshot%202023-09-30%20150225.png)

I noticed that the new vegetation mask derived from Sentinel imagery covers a smaller area compared to the previous Landsat mask, primarily due to differences in spatial resolution. To refine my area estimation, I decided to survey the total area covered by this new mask. Since the output of the raster function does not include a raster attribute table, I created a copy `NDVI_RefinedMask.tif` of the mask to allow me to generate the necessary attribute table and accurately assess the total area covered by the Greater Than raster layer.

After refining the symbology of the resulting mask, I conducted an `area calculation` to quantify the extent of vegetation. 

![water policy](./screenshot%202/Screenshot%202023-09-30%20152131.png)

By building a raster attribute table for the refined mask `NDVI_RefinedMask.tif` using the `Build Raster Attribute Table` tool and calculating the area based on cell counts, 

* `NDVI_RefinedMask.tif` layer `Attribute Table`:

![water policy](./screenshot%202/Screenshot%202023-09-30%20152257.png)

**The count of cells with the value "1" in the attribute table is around 75,000**
**Area of vegetation based on the count of cells and the cell size:**
74,639 x 100 square meters (cell size 10 x 10) = 7,463,900 square meters or `7.4 square kilometers`

For comparison, in the Landsat-based area calculation, the vegetation mask estimated an area of `4.8 square kilometers.`

![water policy](./screenshot%202/Screenshot%202023-09-30%20153411.png)

In the map, there are additional areas visualized in green polygons in the new vegetation mask. These new areas indicate how the estimated vegetation area has changed. Because the new vegetation mask is based on higher-resolution imagery, I was able to identify
smaller vegetation areas not included in the Landsat vegetation mask. 

With a good estimate of the overall total vegetation area, I have created information for decision makers to consider when making any water policy change.
