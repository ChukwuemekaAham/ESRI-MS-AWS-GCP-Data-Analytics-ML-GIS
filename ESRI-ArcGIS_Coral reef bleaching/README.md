## Predicting Coral Reef Bleaching with Multidimensional Data in ArcGIS Pro

This project explores multidimensional sea surface temperature data in the Gulf of Mexico and Caribbean Sea to identify areas vulnerable to coral reef bleaching due to increasing water temperatures. ArcGIS Pro was used to visualize and analyze this data, predicting which coral reefs might be at risk in the future.

**Scenario:**

Coral reefs are vital marine ecosystems, providing food, shelter, and breeding grounds for numerous species.  Increasing ocean temperatures pose a significant threat to these reefs, causing coral bleaching and making them susceptible to other threats. This project utilizes multidimensional sea surface temperature data to predict which areas of coral reefs are most likely to experience prolonged periods of warming, leading to increased bleaching risk. 

**1. Data:**

* Download link: [https://www.arcgis.com/home/item.html?id=efd639b1d97843b59d15473a25225d31](https://www.arcgis.com/home/item.html?id=efd639b1d97843b59d15473a25225d31).

![CoralReefPrediction](./screenshot/Screenshot%202023-10-17%20152508.png)

* `Data` folder - [MultidimensionalData](./MultidimensionalData/).

**2. Create a New ArcGIS Pro Project:**

* `Project` > `Map` >  `New Project` > `CoralReefPrediction` for `Name` of project.

A new ArcGIS Pro project named `CoralReefPrediction` was created. 

**3. Adding the Multidimensional Data:**

I added multidimensional data to my map.

![CoralReefPrediction](./screenshot/Screenshot%202023-10-17%20153858.png)

![CoralReefPrediction](./screenshot/Screenshot%202023-10-17%20154601.png)

![CoralReefPrediction](./screenshot/Screenshot%202023-10-17%20154837.png)

![CoralReefPrediction](./screenshot/Screenshot%202023-10-17%20155136.png)


**Outcome:** The `CoralReefAnalysis.nc_sst` multidimensional raster layer is added to the map and displays the sea surface temperature. 

Sea surface temperature is defined as the water and/or sea ice temperature close to the surface. The water depth ranges from 1 millimeter to 20 meters. The data provider indicates that
the temperature units are Kelvin (K). When converted to Fahrenheit (F), the range of values is between 51.69 degrees F and 87.72 degrees F (284.092 K and 304.108 K). 

For more information about sea surface temperature, go to the S2S Sea Surface Temperature article (https://links.esri.com/SeaSurfaceTemp | https://confluence.ecmwf.int/display/S2S/S2S+Sea+Surface+Temperature).

![CoralReefPrediction](./screenshot/Screenshot%202023-10-17%20155416.png)


**4. Visualizing the Multidimensional Raster Layer:**

In this step, I successfully configured the multidimensional raster layer to visualize sea surface temperature data over time. Accessed available time slices, selected the last one, and then used the time slider to animate the data, visualizing sea surface temperatures for each month of 2022.

![CoralReefPrediction](./screenshot/Screenshot%202023-10-18%20121917.png)

Paused the animation and saved the project, ready to further explore the multidimensional data.

**5. Viewing Temperature Changes Over Time:**

Since the purpose of this analysis is to consider how sea surface temperature changes affect coral reefs, the next step was to add a feature layer to represent the locations of the coral reefs. I then visualize changes in temperature over time both in the map, focusing in on the coral reefs, and in a chart.

1. Added `CoralReefAreas.shp` to current map.

**Outcome:** The `CoralReefAreas` layer was added, displaying polygons representing the coral reef areas.

![CoralReefPrediction](./screenshot/Screenshot%202023-10-18%20125519.png)

![CoralReefPrediction](./screenshot/Screenshot%202023-10-18%20130200.png)

![CoralReefPrediction](./screenshot/Screenshot%202023-10-18%20130345.png)

2. I successfully used the `Temporal Profile` tool to analyze the multidimensional raster dataset   `CoralReefAnalysis.nc_sst` representing sea surface temperature. Selected a point within the Bahamas, generated a chart of the mean temperature values over time, and then `Aggregated` the chart to show `Yearly Maximum Temperatures`. Clicked the `Point` button in the `Define An Area Of Interest` section and added a point within the polygon containing the Bahamas. Expanded the `Aggregation Options` section and set the `Interval Size` to `1 Year`. Changed the `Time Aggregation` to `Maximum`. Added a `Trend line` revealing how maximum temperatures have changed over time within that specific location. 

![CoralReefPrediction](./screenshot/Screenshot%202023-10-18%20133159.png)

![CoralReefPrediction](./screenshot/Screenshot%202023-10-18%20133160.png)


For this particular point, the sea surface temperature appears to rise in value each year. The chart is one way to see the changes in sea surface temperature. There are also ways to determine how these temperatures have trended historically and may trend in the future.


**6. Visualizing the Trend as a Raster:**

The `Generate Trend Raster` tool was used to create a multidimensional raster that estimates the temperature trend for each pixel over the time series. The tool takes into account the cyclical patterns of seasonal temperature changes.

* Right-clicked the `CoralReefAnalysis.nc_sst` layer in the Contents pane and `Zoomed To Layer`.
* On the `Multidimensional` tab, in the `Analysis` group, clicked `Trend` to open the `Generate Trend Raster` tool.

![CoralReefPrediction](./screenshot/Screenshot%202023-10-18%20134321.png)

* Parameters:
    * Input Multidimensional Raster: `CoralReefAnalysis.nc_sst`
    * Output Multidimensional Raster: `..\Data\SST_Trend.crf`
    * Trend Type: `Harmonic`
    * Cycle Unit: `Years`

**Outcome:** The `SST_Trend.crf` layer was added to the map.


![CoralReefPrediction](./screenshot/Screenshot%202023-10-18%20134322.png)

The `positive values` represents an increasing temperature trend (purple), and `negative values` indicates a decreasing trend (green).** 


**7. Predicting Future Sea Surface Temperature Values as a Raster:**

Looking at the multidimensional raster slices individually and viewing the trend as a whole gives an idea of historical changes to sea surface temperature. In this step, I derive a new multidimensional raster data that will predict how sea surface temperature values may change in the future.

1. On the `Multidimensional` tab, clicked `Predict` to open the `Predict Using Trend Raster` tool.
2. Parameters:
   - **Input Trend Raster:** `SST_Trend.crf`
   - **Output Multidimensional Raster:** `..\Data\SST_Predict.crf`
   - **Dimension Definition:** By Interval
   - **Start:** `1980-01-01T00:00:00`
   - **End:** `2030-12-01T00:00:00`
   - **Unit:** Months
3. Clicked `Run`.


**Outcome:** A new multidimensional raster was created, predicting future sea surface temperature values up to the year 2030.

![CoralReefPrediction](./screenshot/Screenshot%202023-10-18%20134311.png)

4. Last time slice in 2030 (`2030-12-01T00:00:00`).
* The `maximum` value listed for the prediction raster is `306.38`.
* The maximum value has `increased` in the prediction raster from the `CoralReefAnalysis.nc_sst layer`.



**8. Identifying Anomalies in Sea Surface Temperature Predictions:**

I identified anomalies in the sea surface temperature predictions using the following steps:

1. On the `Multidimensional` tab, clicked `Anomaly` to open the `Generate Multidimensional Anomaly` tool.
2. Parameters:
   - **Input Multidimensional Raster:** `SST_Predict.crf`
   - **Output Multidimensional Raster:** `..\Data\SST_Anomaly.crf`
   - **Anomaly Calculation Method:** Difference From Mean
   - **Mean Calculation Interval:** Recurring Monthly
3. Clicked `Run`.

**Outcome:** The `SST_Anomaly.crf` layer was added to the map, displaying variations from the monthly mean temperature.

![CoralReefPrediction](./screenshot/Screenshot%202023-10-18%20134323.png)

4. Reviewed the color ramp symbol for the new multidimensional raster, noting the positive and negative values, where positive values indicate temperatures above the mean and negative values indicate temperatures below the mean. In this slice, from January 1980, there are some coral reef areas above the mean, including around Mexico's Yucatan Peninsula.

5. Cycled through different time slices to observe how the anomalies changed over the months and years.

Current display slice at `2030-12-01T00:00:00`

![CoralReefPrediction](./screenshot/Screenshot%202023-10-18%20134324.png)

In this time slice, most of the coral reefs are in areas with higher sea surface temperature anomalies. Although rising
temperatures may be a cause for concern, it is when coral reefs are exposed to prolonged warming that they will experience bleaching. 

**9. Measuring the Duration of Exposure to Warmer Temperatures:**

After predicting the anomalies, next was to determine which areas may be exposed to prolonged rising temperatures and are in danger of
bleaching.

I measured the duration of exposure to warmer temperatures using the following steps:

1. On the `Multidimensional` tab, clicked `Find Argument Statistics` to open the tool.
2. Set the parameters:
   - **Input Multidimensional Or Multiband Raster:** `SST_Anomaly.crf`
   - **Dimension:** `StdTime`
   - **Output Raster:** `..\Data\SST_ArgStatistics.crf`
   - **Statistics Type:** Duration
   - **Dimension Definition:** Interval Keyword
   - **Keyword Interval:** Yearly
   - **Minimum Value:** `0.5`
   - **Maximum Value:** `3`
3. Clicked `Run`.

**Outcome:** The `SST_ArgStatistics.crf` layer was added to the map, indicating the number of months in a year when temperatures are between 0.5 and 3 degrees above average for each location.

![CoralReefPrediction](./screenshot/Screenshot%202023-10-18%20134325.png)


4. Right-clicked the `SST_ArgStatistics.crf` layer in the Contents pane, selected `Symbology`, and changed the `Primary Symbology` from `Stretch` to `Classify`.

**Outcome:** The raster layer was classified into five categories based on the duration of exposure to warming temperatures.

![CoralReefPrediction](./screenshot/Screenshot%202023-10-18%20134326.png)

5. Reviewed the updated symbology and corresponding values, noting areas experiencing prolonged warmer temperatures.

![CoralReefPrediction](./screenshot/Screenshot%202023-10-18%20134327.png)

6. Changed the current display slice to visualized the predicted duration of exposure to warmer temperatures in the future.


* Areas experiencing the most prolonged warmer temperatures, especially those areas that are near coral reefs.

`2023-01-01T00:00:00 - 2023-12-31T23:59:59.914` 

![CoralReefPrediction](./screenshot/Screenshot%202023-10-18%20134328.png)

`2030-01-01T00:00:00 - 2030-12-01T00:00:00`.

![CoralReefPrediction](./screenshot/Screenshot%202023-10-18%20134329.png)


* To find the most affected areas, configured symbology to highlight the significant areas. 

The classification scheme visualizes the areas into three distinct classes.  

- Values symbolized in red indicate that the average sea surface temperature that met the set threshold (0.5 - 3 degrees above the
average) for more than 8 months.

- Values symbolized in orange indicate that the average sea surface temperature that met the set threshold (0.5 - 3 degrees above
the average) that lasted between 2-8 months.

- Values symbolized in yellow indicated that the average sea surface temperature either did not meet the set threshold (0.5 - 3
degrees above average) or if it did, the rise in temperature did not last more than 2 months.

In this prediction for 2030, many of the coral reef areas, especially in the Gulf of Mexico will be experiencing prolonged warmer temperatures.

To learn more about monitoring coral reefs at risk of bleaching, go to ArcGIS Blog: Monitor Coral Bleaching Around the World in Real-Time
(https://www.esri.com/arcgis-blog/products/arcgis-living-atlas/real-time/coral-bleaching-stations/).

**Outcome:** Successfully completed the analysis and visualized critical data on temperature exposure.


**Conclusion:**

I demonstrated how to use ArcGIS Pro to analyze multidimensional sea surface temperature data, predict future trends, and identify areas most vulnerable to coral bleaching. This analysis can help scientists, resource managers, and policymakers understand the potential impact of climate change on coral reefs and inform efforts to mitigate bleaching events.


