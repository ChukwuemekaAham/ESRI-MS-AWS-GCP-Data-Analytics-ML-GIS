## Measuring Land Cover Change Over Time: Analyzing Development in Dallas, Texas

This project utilizes ArcGIS Pro to analyze land cover change around Dallas, Texas, from 2001 to 2016.  The classified thematic rasters and the Change Detection Wizard were use to identify the types and extent of land cover transformation, particularly focusing on the growth of developed areas.

**Scenario:**

You are a GIS analyst for a local government agency interested in understanding how land cover has changed around Dallas, Texas. You have two classified thematic rasters representing aggregated land cover classes from 2001 and 2016, both classified with the same schema. 

**Introduction:**

Understanding land cover change over time is crucial for effective land use planning and policy-making. By analyzing imagery of the same area over several years through image classification, each pixel is assigned a class based on a classification schema.

One of the most popular classification schemas is the National Land Cover Database (NLCD). The NLCD is created by the Multi-Resolution Land Characteristics (MRLC) consortium, which classifies areas based on their land cover. For more information about the
NLCD schema, see the USA NLCD Land Cover layer item page
(https://links.esri.com/USANLCD | https://www.arcgis.com/home/item.html?id=3ccf118ed80748909eb85c6d262b426f).

This method helps measure the type and amount of change, providing valuable insights into the impact of past decisions and aiding future planning. The resulting thematic raster from this process allows for detailed analysis of land development and other changes.

**1. Opening and Analyzing the Dallas Land Cover Evaluation Map Package from ArcGIS Online:**

The map package includes two classified thematic rasters that will be used in the analysis. To aid in change detection, the two rasters have the same modified classification scheme.

I followed these steps to open and analyze the `Dallas Land Cover Evaluation` map package in ArcGIS Pro:

1. Located the `Dallas Landcover Evaluation` map package by Esri Training Services and downloaded it, saving `Dallas_Landcover_Evaluation.mpkx` in my project folder.

2. Opened the `Dallas_Landcover_Evaluation.mpkx` map package in File Explorer.

![dallas](./screenshots/Screenshot%202023-10-17%20102459.png)

**Outcome:** The map package opened in ArcGIS Pro, displaying two classified thematic rasters for land cover in 2001 and 2016 with eight classes based on the NLCD classification schema. 

The eight classes are condensed and slightly modified from the original NLCD classification, as outlined in the following table:

| Condensed Class   | Original NLCD Class                            |
|-------------------|------------------------------------------------|
| Agriculture       | Cultivated Crops                              |
| Barren Land       | Barren Land                                   |
| Developed         | Developed Open Space                          |
|                   | Developed Low Intensity                       |
|                   | Developed Medium Intensity                    |
|                   | Developed High Intensity                      |
| Forest            | Deciduous Forest                              |
|                   | Evergreen Forest                              |
|                   | Mixed Forest                                  |
| Grassland         | Grassland/Herbaceous                          |
|                   | Pasture                                       |
| Open Water        | Open Water                                    |
| Shrub/Scrub      | Shrub/Scrub                                   |
| Wetlands          | Woody Wetlands                                |
|                   | Emergent Herbaceous Wetlands                  |


3. Reviewed the legend of the `NLCD2001_Dallas_Condensed.tif` layer.

**Outcome:** The `Grassland` class was identified as the most prominent land cover in 2001.

4. Opened the `NLCD2001_Dallas_Condensed.tif` attribute table and sorted the `Count` column in descending order.

![dallas](./screenshots/Screenshot%202023-10-17%20110329.png)

**Outcome:** This allowed me to identify the count for the `Developed` class.

5. Turned off the visibility of the `NLCD2001_Dallas_Condensed.tif` layer and opened the `NLCD2016_Dallas_Condensed.tif` attribute table.

6. Sorted the `Count` column in descending order.

![dallas](./screenshots/Screenshot%202023-10-17%20110226.png)

**Outcome:** Identified the count for the `Developed` class in 2016 and compared it to the count in 2001. Noted that the count for the `Developed` class increased from 2001 to 2016. The 2016 layer contains 963,859 more cells than the 2001 layer.

**2. Configuring the Change Detection Wizard:**

I configured the Change Detection Wizard to analyze land cover changes between 2001 and 2016 using the following steps:

1. From the `Imagery` tab, clicked `Change Detection` and selected `Change Detection Wizard`.
2. Set the parameters:
   - **Change Detection Method:** Categorical Change
   - **From Raster:** `NLCD2001_Dallas_Condensed.tif`
   - **To Raster:** `NLCD2016_Dallas_Condensed.tif`
   - **Processing Extent:** Full Extent

   ![dallas](./screenshots/Screenshot%202023-10-17%20132855.png)

3. Clicked `Next`, then chose the `Only` link next to the `Developed` class in the `To Classes` section.

![dallas](./screenshots/Screenshot%202023-10-17%20133207.png)

4. Selected `From Color` for the `Transition Class Color Method` and clicked `Preview`.
5. Turned off the visibility of the `NLCD2016_Dallas_Condensed.tif` layer.

**Outcome:** The map displayed a preview layer highlighting areas where land cover has changed.

![dallas](./screenshots/Screenshot%202023-10-17%20134042.png)


6. Reviewed the preview layer legend and opened the `Preview_ComputeChange` attribute table.

![dallas](./screenshots/Screenshot%202023-10-17%20134214.png)

**Outcome:** The table showed land cover classes that transitioned to new classes.

7. Zoomed to the `Frisco, TX` bookmark and identified primary classes that converted to `Developed`.

**Outcome:** Observed that `Agriculture` and `Grassland` classes likely transitioned to `Developed` areas. Agriculture and Grassland classes  Developed

8. Closed the attribute table and clicked `Next` in the wizard.
9. In the `Output Generation` step, set `Smoothing Neighborhood` to `None` and confirmed `Save Result As` was set to `Raster Dataset`.
10. Clicked `Browse` for the output dataset, named it `DallasDevelopedChange.tif`, and saved it to `Data` directory.
11. Clicked `Run` and then right-clicked `DallasDevelopedChange.tif` to select `Zoom To Layer`.

![dallas](./screenshots/Screenshot%202023-10-17%20135253.png)


**Outcome:** A new raster layer was created, showing areas that transitioned to Developed land cover. The raster output shows all the areas in the raster that have changed and the classes from which they have changed. Developed areas have expanded from 2001 to 2016, and this analysis indicates where the growth has occurred.


12. Clicked `Finish` in the Change Detection Wizard.

**Outcome:** Successfully completed the Change Detection Wizard.


**3. Change in the Developed Areas:**

* `DallasDevelopedChange.tif` attribute table

![dallas](./screenshots/Screenshot%202023-10-17%20140023.png)

The `Other` and `No Change` classes have the highest counts. Although they have the highest count values, these two are ignored, because I am only interested in specifically named classes that converted to Developed

* **The `Grassland` class had the most cells converted to `Developed` area.** 

* **`111,374` cells changed from `Agriculture` to `Developed`.**

**Outcome:** The results indicate that areas classified as Grassland and Agriculture have been converted to Developed land more than other
land classes

* `DallasDevelopedChange.tif` layer properties > `Raster Information` . 

![dallas](./screenshots/Screenshot%202023-10-17%20140057.png)

* **Total area of the Agriculture class that converted to Developed.**
Based on the cell size The total area of the Agriculture class that converted to the Developed class is 100,236,600 square meters (111,374 x 900).


With the Change Detection Wizard, I was able to discover which classes converted to the Developed class from 2001 to 2016. Also
determined the total area that was converted for each class.
