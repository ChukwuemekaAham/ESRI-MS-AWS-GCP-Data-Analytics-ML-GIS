## Using Remote Sensing for Fossil Exploration: Identifying Ferrous Mineral Concentrations

This project utilizes ArcGIS Image for ArcGIS Online to analyze multispectral imagery and create a thematic raster that highlights areas with concentrated ferrous minerals, aiding paleontologists in their fossil exploration efforts. Fossil exploration is a challenging process that can be aided by remote sensing.


**Scenario:**

Imagine you are a GIS analyst assisting a group of paleontologists in locating potential fossil sites in Montana.  You will use ArcGIS Image for ArcGIS Online to create a thematic raster that highlights areas with high concentrations of ferrous minerals within a defined study area.

**1. Open an Imagery Layer in a Web Map:**

I started the process by adding the imagery layer to a web map on ArcGIS Online. Opened the `Preliminary Fossil Exploration Landsat tiled imagery` layer in the Map Viewer. This layer rendered with the Natural Color band combination.

![Screenshot 2023-10-20 135934.png](./screenshot/Screenshot%202023-10-20%20135934.png)

The map was saved by clicking `Save And Open`, selecting `Save As`, and entering the following details:
* Title: `Fossil Exploration [\initials]`
* Tags: `Imagery in Action`, `Esri`, `fossil`
* Summary: `Web map for fossil exploration in the Imagery in Action MOOC`.

**Outcome:** Saved copy of the web map will be used for the analysis.

**2. Review the Imagery Layer:**

In this step, I reviewed the imagery layer and changed the symbology to make potential fossil areas more visible.

* `Preliminary Fossil` layer.
* `RGB` > `Style Options`, the following combination was selected:
    * Red: `ShortwaveInfrared_1`
    * Green: `NearInfrared`
    * Blue: `Blue`
* `Standard Deviation` for `Stretch Type`.
* `Apply Dynamic Range Adjustment` option enabled.

![Screenshot 2023-10-20 141119.png](./screenshot/Screenshot%202023-10-20%20141119.png)

This raster band combination uses the `Shortwave Infrared` and `Near Infrared` bands to more easily view and extract geologic
features. Adding Dynamic Range Adjustment (DRA) allows for optimal display of the full range of pixels in the image. The various geologic structures are more visible due to the contrasting colors, giving a visualization of the various types of surfaces that are present in the imagery layer

![Screenshot 2023-10-20 141629.png](./screenshot/Screenshot%202023-10-20%20141629.png)

**Outcome:** Zoomed in on a burn scar, which appears darker than the surrounding area and saved the map with the updated rendering.

The area is much darker than the surrounding area, evidence of a burn scar from a wildfire. The Shortwave Infrared and Near
Infrared raster bands in this band combination can also be used to discover burned areas. 

**Deduction:**
In my analysis, the pixel values associated with burn scars will be considered to avoid including those locations in the search
for potential ferrous minerals.

**3. Create a Thematic Raster using a Raster Function:**

In this step, a raster function was used to create a thematic raster that will highlight the areas containing ferrous mineral
concentrations.

* `Settings toolbar` > `Analysis` > `Raster Functions` > `band`.
* `Band Arithmetic` to open the `Band Arithmetic` raster function pane.

The Band Arithmetic function allows to perform arithmetic functions on the bands of an input raster layer. We can specify
your own formula or input a predefined method. 

* The `Ferrous Minerals ratio` method, which divides pixel values from the Shortwave Infrared band by pixel values from the Near Infrared band according to the following formula: `FM = SWIR / NIR`, was added.


I utilized the `Band Arithmetic` raster function to create a new imagery layer highlighting areas with high concentrations of ferrous minerals. I selected the `Preliminary Fossil Exploration Landsat` raster, chose the `Ferrous Minerals` method, and entered `B6 B5` for the band indexes. 

![Screenshot 2023-10-20 145020.png](./screenshot/Screenshot%202023-10-20%20145020.png)

Once processing was complete, I zoomed to the `Output` layer, opened the `Ferrous_Minerals Fields` pane, and set the pixel value formatting to `2 Decimal Places`. The layer was displayed with a `Stretch` renderer, indicating higher values with lighter colors.

![Screenshot 2023-10-20 145755.png](./screenshot/Screenshot%202023-10-20%20145755.png)

I then examined the burn scar area, noting that most pixel values exceeded 1.3, and zoomed out to visualize the entire `Ferrous Mineral` imagery layer. Finally, I saved the map, successfully creating and visualizing the `Output` layer.

![Screenshot 2023-10-20 145939.png](./screenshot/Screenshot%202023-10-20%20145939.png)

![Screenshot 2023-10-20 150702.png](./screenshot/Screenshot%202023-10-20%20150702.png)


The paleontologists have informed that locations with ferrous minerals should have a pixel value greater than 1.15. I
observed that the majority of pixels in the burn scar have values above 1.3. The ideal range of values to locate ferrous minerals
should be between 1.15 and 1.3. This knowledge will allow to locate areas with high concentrations of ferrous minerals
while excluding burn scar locations. Next I create a function to identify areas meeting the specified criteria.

**4. Add the First Raster Function:**

Raster functions was used to identify areas of concentrated ferrous minerals. To discover the desired areas, I created a
selection that will reveal the areas that fall within 1.15 to 1.3.

In this step I configured the first function to find the areas with values greater than 1.15, by creating a `New Raster Function Template`

![Screenshot 2023-10-20 152254.png](./screenshot/Screenshot%202023-10-20%20152254.png)

**Outcome:** Added a raster function to the template that specifies the lower limit (1.15) for identifying areas with concentrated ferrous minerals.

**5. Add the Second Raster Function:**

In this step, I added a second raster function to the Raster Function Template. This raster function will identify pixels in the
input raster with values less than or equal to 1.3. Excluding pixels with values greater than 1.3 will prevent most burn scar areas
from being included in the identification of potential fossil locations

![Screenshot 2023-10-20 152642.png](./screenshot/Screenshot%202023-10-20%20152642.png)

![Screenshot 2023-10-20 154638.png](./screenshot/Screenshot%202023-10-20%20154638.png)

**Outcome:** Added a second raster function to the template, setting an upper limit (1.3) to exclude areas with high values (likely burn scars).


**6. Combine Raster Functions in a Raster Function Template:**

After setting an upper and lower threshold for raster values, I can combine the raster functions to specifically locate
values between both thresholds.

![Screenshot 2023-10-20 155446.png](./screenshot/Screenshot%202023-10-20%20155446.png)

![Screenshot 2023-10-20 155646.png](./screenshot/Screenshot%202023-10-20%20155646.png)

**Outcome:** Created a `Raster Function Template` that combines the two functions, identifying areas with ferrous mineral concentrations within the specified range.

**7. Run the Raster Function Template:**

![Screenshot 2023-10-20 155906.png](./screenshot/Screenshot%202023-10-20%20155906.png)

I opened the `Fossil Exploration` web map in Map Viewer and accessed the Analysis tools to utilize the `Possible Ferrous Mineral Locations` raster function template. I set the input raster and the output name, and ran the process to highlight potential fossil locations.

![Screenshot 2023-10-20 160605.png](./screenshot/Screenshot%202023-10-20%20160605.png)

![Screenshot 2023-10-20 160754.png](./screenshot/Screenshot%202023-10-20%20160754.png)

**Outcome:** The raster function template after processing, creates a new layer that highlights potential fossil locations.

After processing, I adjusted the style of the `Prospective_Locations` layer by applying unique colors, setting areas with potential ferrous mineral concentrations to blue.

![Screenshot 2023-10-20 161304.png](./screenshot/Screenshot%202023-10-20%20161304.png)


**8. Add Mask** 

I explored the possibility of enhancing the template by adding the `Mask` raster function and connecting it to the output from `Boolean And`, reviewing the ArcGIS Online Help for proper parameters before saving and executing the updated raster function.

![Screenshot 2023-10-20 163923.png](./screenshot/Screenshot%202023-10-20%20163923.png)

![Screenshot 2023-10-20 163932.png](./screenshot/Screenshot%202023-10-20%20163932.png)

**Outcome:** The output only display the pixel values of potential ferrous mineral locations, excluding areas outside the specified range and areas with high values.

![Screenshot 2023-10-20 164007.png](./screenshot/Screenshot%202023-10-20%20164007.png)

![Screenshot 2023-10-20 164801.png](./screenshot/Screenshot%202023-10-20%20164801.png)

![Screenshot 2023-10-20 172319.png](./screenshot/Screenshot%202023-10-20%20172319.png)
