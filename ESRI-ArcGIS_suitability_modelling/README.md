##  Suitability Modeling for a Carbon-Neutral Headquarters in Vermont

This project uses ArcGIS Pro's suitability modeling capabilities to identify the most suitable location for a carbon-neutral corporate headquarters in Vermont.  The project involves evaluating various factors to determine the best location that minimizes environmental impact and is attractive to prospective employees.

**Methodology:**

1. **Define the problem:** Defining the problem will help to identify a specific and measurable goal for the suitability analysis.
2. **Identify the criteria:** The subject of the suitability model will respond to different phenomena, referred to as criteria (for example, slope). The criteria should support the defined goal of the suitability model.
3. **Derive the criteria:** If no data that represents each criterion, derive the criteria from a base dataset (for example, a slope criterion is derived from an elevation base dataset).
4. **Transform criteria values:** Criteria values are measured using different scales, so we must transform these values to a common scale so that they can be compared and combined.
5. **Weight and combine criteria:** Some criteria may be more important than others. Weight the criteria relative to one
another before combining them to create a single suitability layer.
6. **Locate the site:** The suitability layer reflects the characteristics of a location. Integrate the spatial requirements of the subject of the suitability model and use these spatial requirements to identify the best locations from the suitability layer.
7. **Analyze the results:** Analyze the results to confirm that the selected site meets the requirements and ensure that the goals of the analysis are achieved.

**Scenario:**

A global company wants to establish a carbon-neutral headquarters in Vermont. The owner prioritizes a location that minimizes the building's carbon footprint and is appealing to potential employees.  This project will utilize suitability modeling techniques to pinpoint the optimal location in Vermont.

**1. Define the Goal:**

* The goal is to choose a location for a corporate headquarters that has a minimal carbon footprint and is situated and designed in a way that is attractive to prospective employees.

**2. Identify the Criteria:**

A comprehensive list of criteria is established, categorized into objectives, to ensure a well-rounded suitability analysis.

* Four objectives and corresponding criteria are identified:

| Criteria                                           | Required data                                | Derived criteria layer name |
|----------------------------------------------------|---------------------------------------------|------------------------------
| **Building Site**                           |                                            |                             |
| Wetlands and high-density areas are less preferred | Land-use layer                               | LandUse                      |
| Steep slopes are less preferred                  | Elevation layer                             | Slope                        |
| Closer to major roads is preferred                | Distance from major roads layer            | Dist_MRoads                  |
| Visibility from major roads is less preferred       | Viewshed layer                              | Views                        |
| **Energy independence**                           |                                            |                              |
| Higher solar radiation potential is preferred      | Solar radiation potential layer           | Solar                        |
| Closer to electric lines (to connect solar energy to the utility grid) is preferred | Electric distributions layer               | Dist_Elect                   |
| South-facing angles are more preferred              | Aspect layer                                | Aspect                       |
| **Access to amenities**                           |                                            |                              |
| Closer to the airport and the city of Burlington is preferred | Airport locations layer                      | Dist_Airport                  |
| Closer to recreational areas is preferred         | Recreation layer                            | Dist_Rec                     |
| Closer to residential areas is preferred         | Residential density layer                  | Dist_Resident                 |
| **Environmental concerns**                       |                                            |                              |
| Farther from protected areas is preferred         | Protected areas layer                       | Dist_Protect                  |
| Farther from biological areas is preferred        | Biological areas layer                     | Dist_Biol                    |
| Farther from wetlands is preferred               | Wetlands layer                             | Dist_Wetlands                 |
| Farther from streams is preferred                | Streams layer                              | Dist_Streams                  | 

These criteria were chosen for this project and are not intended to be an exhaustive list of
the criteria that are used in this type of suitability model

**4. Open an ArcGIS Pro Project:**

* Start ArcGIS Pro.
* Sign in using the provided course ArcGIS account.
* From the Start page, click Open Another Project.
* Browse to the `Suitability` folder you saved on your computer.
* Select the `Headquarters_Siting.aprx` project and click OK.

![Screenshot 2023-09-16 183826.png](./screenshot/Screenshot%202023-09-16%20183826.png) 

The ArcGIS Pro project includes a map of Vermont with a layer that outlines the AOI, or study area, for this suitability model.
This study area spans across several counties in Vermont, including the cities of Burlington, Hinesburg, and Stowe. 

A mountain range, called the Green Mountains, runs north to south in the eastern part of the study area. The map includes additional layers that represent the other datasets required to locate the most suitable location for the corporate
headquarters.

* These are the work layers:
    - MajorRoads
    - GreenMTRidge
    - Views_Zero
    - LandUse
    - Elevation_30

The Study_Mask layer is a dataset that defines which locations in the inputs will be considered in the execution of the tool.

**5. Derive a Criterion:**

Each criterion in a suitability model begins with a base dataset. The base dataset can be used as the criterion dataset, or it
can be used to derive the required criterion dataset. 

### Building Site objective

* `Slope` This layer represents one of the criteria for the "Building Site" objective. In this step, the elevation base dataset was used to derive a slope layer for the study area. 

* The `Surface Parameters (Spatial Analyst Tools)` tool was used to derive the slope, or gradient, for each cell in the
Elevation_30 base data.

* Parameters:
    * Input Surface Raster: `Elevation_30`
    * Output Raster: `Slope`
    * Parameter Type: `Slope` 

![Screenshot 2023-09-16 201630.png](./screenshot/Screenshot%202023-09-16%20201630.png) 

The Slope layer is added to the map. The Neighborhood Distance parameter is set to 30 Meters to match the cell size of the input surface raster. The cells in this raster are symbolized in colors ranging from black, indicating gentler slopes, to white, indicating
steeper slopes. To learn more about the Surface Parameters tool, go to ArcGIS Pro Help: Surface Parameters (Spatial Analyst).

* `Dist_MRoads`

* The `Distance Accumulation (Spatial Analyst Tools)` tool was used to calculates the straight-line, or Euclidean, distance from the major roads. The study area for this analysis includes the
Green Mountain Ridge. Cars must drive around the ridge, which you have indicated by adding it as a barrier. 

* Parameters:
    * Input Raster Or Feature Source Data: `MajorRoads`
    * Output Distance Accumulation Raster: `Dist_MRoads`
    * Input Barrier Raster Or Feature Data: `GreenMTRidge`

![Screenshot 2023-09-16 202819.png](./screenshot/Screenshot%202023-09-16%20202819.png) 

**Outcome:** 
The resulting `Dist_MRoads`
layer illustrates the accumulated distance from major roads, where green indicates shorter distances and yellow to pink
indicates farther distances. Areas around the ridge may be relatively close (straight-line distance) to a major road. However,
the Distance Accumulation tool indicates that these areas are far from major roads because you would have to drive around
the ridge. 

To learn more about the Distance Accumulation tool, go to ArcGIS Pro Help: Distance Accumulation (Spatial
Analyst).

![Screenshot 2023-09-16 203739.png](./screenshot/Screenshot%202023-09-16%20203739.png) 

The `MajorRoads` and `Views_Zero` layers were visually reviewed, which represent criteria for the "Building Site" objective. 

The Views_Zero layer shows visibility from major roads. According to the building site criteria, visibility from major roads is
less preferred. Areas that are not visible from major roads have a cell value of zero and are represented using black. As the
cell value increases, the symbology lightens to gray and eventually white. The white areas are the most visible from the major
roads, making them the least preferable areas.


* `LandUse` 

![Screenshot 2023-09-16 205245.png](./screenshot/Screenshot%202023-09-16%20205245.png) 

The LandUse dataset can be used directly as the criterion, so no geoprocessing tool was necessary to derive any criterion
from this base data.


**7. Create a Submodel:**

You will complete the remaining steps using the Suitability Modeler. The Suitability Modeler is an interactive, exploratory
environment for creating and evaluating a suitability model. In general, constructing a suitability model is a nonlinear,
iterative process. The Suitability Modeler provides analytical feedback at each stage of the suitability modeling process and
allows seamless back-and-forth movement between each stage of the model development. 

To learn more about the
Suitability Modeler, go to ArcGIS Pro Help: What is the Suitability Modeler?

ArcGIS Pro 3.1 allows you to work with submodels when using the Suitability Modeler. When creating a suitability model, you
make trade-offs between individual criteria and their importance (or weight). That is also true for competing objectives. Each
objective can be captured in a different submodel and then combined to create a final suitability model.
In this step, you will create the submodel for the building site objective.


* `Suitability Modeler` The Suitability Modeler tab is
where you can adjust settings and save the model. The Suitability Modeler pane is where you will transform criteria values,

* By unchecking the `Auto Calculate` option, the model data will not automatically update every time a parameter is changed.

* Parameters:
    - Model Name: `HQ_Building_Site` 
    - Output Suitability Raster: `HQ_Building_Site`
    ![Screenshot 2023-09-17 000437.png](./screenshot/Screenshot%202023-09-17%20000437.png)

**Outcome:**   A submodel for the "Building Site" objective was created. A group layer called `HQ_Building_Site` is added to the Contents pane.

**8. Transform Categorical Criteria for a Submodel:**

The values of the criteria datasets are relative to the criteria that they represent. Land use utilizes categorical values, such as
open water, whereas slope uses continuous values ranging from 0 through 90. Before you can weight these criteria relative to
each other, you must transform their values to a common scale. In this step, you will transform the land-use layer.

![Screenshot 2023-09-17 003034.png](./screenshot/Screenshot%202023-09-17%20003034.png)

**Outcome:** The `LandUse` raster dataset was selected from the `Data.gdb` to add `LandUse` layer to the Criteria table and displayed on the map. It was also added to the `HQ_Building_Site` group layer.

* `Transformation` 

The `Suitability` values for each category was adjusted as needed.

| Class | Category                     | Suitability |
|-------|------------------------------|-------------|
| 1     | Open Water                   | 1           |
| 2     | Developed, Open Space        | 5           |
| 3     | Developed, Low Intensity     | 4           |
| 4     | Developed, Medium Intensity   | 3           |
| 5     | Developed, High Intensity    | 1           |
| 6     | Barren Land                  | 8           |
| 7     | Deciduous Forest             | 8           |
| 8     | Evergreen Forest             | 7           |
| 9     | Mixed Forest                 | 8           |
| 10    | Shrub/Scrub                  | 9

SMEs who are working on the building site submodels have decided on the suitability rankings in the table for the land-use
categories.

This table defines the preference scale for each category, where 1 is not preferable and 10 is very preferable.


**Outcome:** The `LandUse` layer was then transformed to a common suitability scale, with values ranging from 1 (not preferable) to 10 (highly preferable).  The most preferred land use categories was displayed in green on the `Transformed LandUse` layer, while the least preferred categories was in red.

![Screenshot 2023-09-17 074809.png](./screenshot/Screenshot%202023-09-17%20074809.png)

* Using the `Suitability Analysis` group, the model was calculated. and saved to the submodel.

**9. Transform Continuous Criteria for a Submodel:**

In this step, you will transform the criteria with continuous values, such as slope, for the building site submodel. Data with
continuous values is known as continuous data, or a continuous surface. This type of data is not spatially discrete, and the
transition between possible values on a continuous surface is without abrupt or well-defined breaks between values.

* `Add Raster Criteria As Layers`
* Added layers:
    * `Dist_MRoads`
    * `Slope`
    * `Views_Zero`


* `Slope`. 

![Screenshot 2023-09-17 082443.png](./screenshot/Screenshot%202023-09-17%20082443.png)

The Suitability Modeler identifies that the Slope layer
is represented by continuous values, so the Continuous Functions method is automatically selected in the Transformation
Pane. This method applies linear and nonlinear functions to transform the values continuously to the suitability scale. 

* Applying `Continuous Functions` transformation methed using `Small` for Function.

As you explore the methods and functions and their parameters, the transformation histogram of the layer, the distribution of
suitability histogram, and the transformed and final suitability map layers in the HQ_Building_Site group layer are updated.
This process provides feedback about the effects that the transformation will have on the transformed criterion as well as the
impact on the final suitability map for your submodel.

In this example, the item that is being modeled is the location for a corporate headquarters, and the criterion is slope. The
preference decreases as the slope increases, which means that the MSSmall function is the best function for this
transformation. The MSSmall function rescales input data based on the mean and standard deviation where smaller values in
the input raster have higher preference. To learn more about the transformation functions, go to ArcGIS Pro Help: The
transformation functions available for Rescale by Function.

![Screenshot 2023-09-17 091422.png](./screenshot/Screenshot%202023-09-17%20091422.png)

**Outcome:** The `Transformed Slope` layer is set to a common preference scale ranging from 1 to 10, where 1 is not preferable and 10 is
very preferable. The most preferred areas are in green and the least preferred areas are in red, with areas of gentler slopes (lower values) displayed in green and steeper slopes (higher values) displayed in red.


* `Dist_MRoads`.
*  `Small` for Function.

![Screenshot 2023-09-17 091918.png](./screenshot/Screenshot%202023-09-17%20091918.png)

**Outcome:** The `Transformed Dist_MRoads` layer was updated, with areas closer to roads displayed in green and areas farther from roads displayed in red.

* `Views_Zero`.
* `LogisticDecay` for Function.

The visibility from roads uses logistic decay to indicate that preference decreases the more visible the site is to the road.

![Screenshot 2023-09-17 092102.png](./screenshot/Screenshot%202023-09-17%20092102.png)

**Outcome:**  The `Transformed Views_Zero` layer is set to a common preference scale ranging from 1 to 10, where 1 is not preferable and
10 is very preferable. The most preferred areas are in green and the least preferred areas are in red, with areas less visible from roads displayed in green and areas more visible from roads displayed in red.


![Screenshot 2023-09-17 094911.png](./screenshot/Screenshot%202023-09-17%20094911.png)


I successfully transformed all the criteria for the "Building Site" submodel to a common suitability scale


**10. Weight the Criteria for a Submodel:**

Certain criteria in the submodel may be more important than others. The application of weights enables the ability to account
for the importance of each criterion to the objective. To account for these differences, you will weight the criteria relative to
one another before combining them.

In ArcGIS Pro, two different methods can be used to weight the criteria: multiplier or percent. When you created the
HQ_Building_Site group layer, the multiplier method was selected to weight the criteria. The transformed criterion values are
multiplied by the value that is specified in the Criteria table in the Suitability Modeler pane. The multiplied transformed
criterion values are then added together. A weight of 2 means that the criterion is twice as important as a criterion with a
weight of 1. A weight of 10 means that the criterion is 10 times more important. Common weights are between 1 and 2. This
method is best when you can directly weight the criteria relative to one another.


* `HQ_Building_Site` layer.
* `Weight` values for each criterion as shown in the table:

**Input Rasters Weight:**

| Input Rasters                    | Weight |
|----------------------------------|--------|
| Slope                          | 1.6    |
| Dist_MRoads                    | 1.25   |
| LandUse                       | 1.6    |
| Views_Zero                    | 1.25   |

Many different approaches are available for determining weights for a specific submodel, which may require collaboration
with SMEs

![Screenshot 2023-09-17 100824.png](./screenshot/Screenshot%202023-09-17%20100824.png)

The values in the suitability surface are calculated as the weighted sum of the values in the transformed data. The higher the
value, the more preferred the location is for the corporate headquarters site.

**11. Combine the Submodels:**

You created the submodel for the building site objective. Other SMEs have created and shared three more submodels with
you. The submodels have already been transformed to a common suitability scale, and it is a best practice to use the same
suitability scale and weight method (multiplier or percent). 

In this step, you will combine the four submodels.

An effective way to work with submodels is to create them in the same Suitability Modeler container (.sam). The
HQ_Building_Site submodel is listed in the Suitability.sam container along with the three other submodels that you will
combine.

* The `HQ_Building_Site` submodel along with the other three submodels that represent the remaining objectives were selected from the `Suitability.sam` container.

![Screenshot 2023-09-17 100824.png](./screenshot/Screenshot%202023-09-17%20101453.png)

`New Suitability Model` group was created to combine all four submodels.
* Parameters:
    * Model Name: `HQ_Combined_Model`
    * Model Input Type: `Submodels`
    * Output Suitability Raster: `HQ_Final_Suitability`

![Screenshot 2023-09-17 103909.png](./screenshot/Screenshot%202023-09-17%20103909.png)

* `Add Raster Submodels As Layers` and `Add Raster Submodel Datasets`.
* `Input Rasters` were selected from the `Suitability_Submodels.gdb`:
    * `HQ_Access_to_Amenities`
    * `HQ_Energy_Independence`
    * `HQ_Environmental_Concerns`

![Screenshot 2023-09-17 104411.png](./screenshot/Screenshot%202023-09-17%20104411.png)

All four submodels are now added to the `Submodels` table.

The SMEs already weighted the criteria for their submodels, so you do not need to weight each submodel. You can explore
the weights they used in each submodel by opening the submodel from the Suitability.sam container in the Catalog pane.


**Outcome:** After combining all four submodels, I ran the model to create the `HQ_Final_Suitability` map at full resolution.

* Visualizing `World Topographic Map` and the `HQ_Final_Suitability` layer in the `HQ_Combined_Model` group layer.

![Screenshot 2023-09-17 105158.png](./screenshot/Screenshot%202023-09-17%20105158.png)


**12. Locate the Site:**

The corporate shareholders have indicated that they want the headquarters to be a campus with five buildings within walking
distance of each other. After further research and discussion, you used this information to define the following spatial requirements:
* The site must include 500 hectares of total area.
* The areas will be divided into five different areas, or regions.
* No two regions can be closer than 0.5 kilometers or farther than 2 kilometers.

The `Locate` tool use the `HQ_Final_Suitability` map to identify five optimal regions based on the specified spatial requirements (total area, number of regions, distance between regions), and the `Suitable_Locations` layer was added to the map.

* Parameters:
    * Input Suitability Map: `HQ_Combined_Model\HQ_Final_Suitability`
    * Area Units: `Hectares`
    * Total Area: `500`
    * Output Raster: `Suitable_locations`
    * Number Of Regions: `5`
    * Region Shape: `Circle`
    * Shape/Utility Tradeoff (%): `50`
    * Evaluation Method: `Highest Average Value`
    * Minimum Distance Between Regions: `0.5`
    * Maximum Distance Between Regions: `2`
    * Distance Units: `Kilometers`

![Screenshot 2023-09-17 110336.png](./screenshot/Screenshot%202023-09-17%20110336.png)

* Visualizing the  `Headquarters` using `Suitable_Locations`, `HQ_Final_Suitability`, and `World Topographic Map` layers.

![Screenshot 2023-09-17 122712.png](./screenshot/Screenshot%202023-09-17%20122712.png)

**Outcome:**  The map shows the best locations for the five building sites.  The five regions are located within the dark green areas of the `HQ_Final_Suitability` layer.

**13. Analyzing the Results:**

* `HQ_Building_Site` group layer.
* Selecting `Suitable_Locations` layer.

* The `Swipe` tool was used to compare the `Suitable_Locations` and `Transformed Views_Zero` layers which revealed that the chosen locations have limited visibility from major roads, and aligns with the criteria

* Comparing the `Suitable_Locations` and `Slope` layers, reveal that the chosen locations are situated in areas with gentler slopes, which aligns with the "Building Site" criteria.

Overall, the site locations meet the requirements for a corporate headquarters that has a minimal carbon footprint.

### Further Analysis
A second part of the goal for the suitability analysis is that the location should be situated and designed in a way that is attractive to
prospective employees. To complete the second part of the analysis, move on to the stretch goal to identify the most suitable
network of paths that can connect the five headquarters buildings to each other and to the park. Employees can then walk or
bike between the campus buildings and the park.

### Case

The shareholders would also like the headquarters to connect to a nearby park so that employees can walk or bike between
the campus buildings and the park. In this analysis, you will identify the best paths, or corridors, using ModelBuilder.

ModelBuilder allows us to visualize and record a series of analyses, or a model. It uses shape, color, text, and symbols to
visually communicate information about the model. ModelBuilder helps you organize, document, and share the analysis
with others.

The two models used are:

* Cost Surface: This model identifies the cost that a traveler (walker or biker) encounters as they move through each cell.
The criteria that the traveler prefers include fewer steep slopes, being farther from roads, and being closer to streams. The
preferred values are assigned a lower cost. The result is a cost surface identifying the cost to move through each cell with
the most preferred areas having lower values. This model is the reverse of a suitability model.

* Connect Campuses: This model converts the park from a vector polygon to a raster, adds the park to the layer with the
five headquarters buildings, and then runs a connectivity tool. The tool connects the five headquarters buildings and park
by using the cost surface created in the previous model. The result identifies the most suitable network of paths that can
connect the buildings to each other and to the park

![Screenshot 2023-09-17 124552.png](./screenshot/Screenshot%202023-09-17%20124552.png)

* **Outcome:**
    ![Screenshot 2023-09-17 122959.png](./screenshot/Screenshot%202023-09-17%20122959.png)
