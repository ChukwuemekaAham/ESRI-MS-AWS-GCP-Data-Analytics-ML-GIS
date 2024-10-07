## Mapping Building Footprints with Deep Learning in ArcGIS Pro

This project utilizes a pre-trained deep learning model from ArcGIS Living Atlas to extract building footprints from a NAIP imagery layer. I explored the process of using this model, adjusting parameters to improve the results, and visualizing the extracted building footprints. 

**Scenario:**

You are a GIS analyst for Henderson County in Texas, tasked with updating the county's GIS data. You have been provided with an imagery layer from the National Agriculture Imagery Program (NAIP) and will use a deep learning package from Esri to extract building footprints.

## Steps taken

**1. Web Map Creation for Building Extraction:**

To create a web map for building extraction in Athens, Texas, I followed these steps:

1. Clicked the `Map` button to open a new web map in Map Viewer.
2. In the `Layers` pane, clicked `Add` to search and add layers.
3. Selected `ArcGIS Online` from the `My Content` dropdown.
4. Searched for `AthensTX_2018` and added the tiled imagery layer to the web map.

![Screenshot 2023-10-25 105139.png](./screenshot/Screenshot%202023-10-25%20105139.png)


**Outcome:** The imagery layer appeared in the web map, rendered with the Natural Color band combination.

#### The manager recommended that I map building footprints in a certain area, so I added a focus area layer to the map.

5. Cleared the search field and typed `building footprint focus`, then added the `Building Footprint Focus Area` feature layer by Esri Training Services and zoomed to the `Building Footprint Focus Area` layer.

![Screenshot 2023-10-25 110334.png](./screenshot/Screenshot%202023-10-25%20110334.png)

6. Saved the map by clicking `Save And Open`, selecting `Save As`, and entering:
   - **Title:** `Building Extraction [initials]`
   - **Tags:** `Imagery in Action`, `Esri`, `Texas`
   - **Summary:** `Web map for building extraction in Athens, Texas.`

**Outcome:** Successfully saved a copy of the web map.

**2. Building Footprint Extraction Process:**

To extract building footprints from the AthensTX_2018 imagery, I followed these steps:

1. On the Settings toolbar, clicked the `Analysis` button to open the `Analysis` pane.
2. Clicked `Tools`, expanded the `Use Deep Learning` section, and selected the `Detect Objects Using Deep Learning` tool.
3. In the tool pane, added the `AthensTX_2018` layer as the input.
4. Under `Model Settings`, selected the `Building Footprint Extraction - USA` deep learning package from the Living Atlas.

![Screenshot 2023-10-25 115429.png](./screenshot/Screenshot%202023-10-25%20115429.png)

![Screenshot 2023-10-25 120038.png](./screenshot/Screenshot%202023-10-25%20120038.png)

**Outcome:** The deep learning model arguments were populated.

5. Typed `AthensTestDeepLearning_[initials]` for the `Output Name`.
6. Set the `Processing Extent` to `Layer` and selected `Building Footprint Focus Area` for both `Processing Extent` and `Mask`.
7. Left the remaining defaults, and clicked `Run`.

![Screenshot 2023-10-25 120724.png](./screenshot/Screenshot%202023-10-25%20120724.png)

**Outcome:** The tool began processing to extract building footprints from the NAIP imagery.

8. After processing, I checked the status and observed the new feature layer in the `Layers` pane.

![Screenshot 2023-10-25 121020.png](./screenshot/Screenshot%202023-10-25%20121020.png)

**Outcome:** A new layer named `AthensTestDeepLearning_[initials]` was added, displaying blue polygons representing the extracted building footprints.

9. Finally, I saved the map.

**Outcome:** Successfully saved the map with the extracted building footprints. The deep learning model arguments are additional parameters that can be adjusted as needed to improve your analysis. They are populated by the tool from reading the Python module on the raster analysis server. Each argument is specified by the deep learning package that you choose. These arguments in the deep learning model are the ones used in the Building Footprint Extraction - USA package.

The confidence threshold is currently set to 0.9. This threshold means that if the model is at least 90 percent certain that a
feature is a building, it will include it in the output. 

I ran the model with the default threshold and then determine whether it needs to be adjusted lower when you review the output.

For more information about deep learning models, go to ArcGIS Enterprise Help: Deep learning in Raster Analysis: Esri model definition file

**3. Review of Extracted Buildings:**

To review the extracted building footprints from the `AthensTestDeepLearning_[initials]` layer, I completed the following steps:

1. In the `Layers` pane, clicked the `Options` button for the `AthensTestDeepLearning_[initials]` layer and selected `Show Table`.

![Screenshot 2023-10-25 122047.png](./screenshot/Screenshot%202023-10-25%20122047.png)

**Outcome:** The attribute table for the extracted buildings opened.

2. Identified the two key fields in the attribute table: `Class` and `Confidence`.
3. Clicked the `Options` button for the `Confidence` field header and selected `Information`.
4. Reviewed the `Statistics` section of the `Confidence` pop-up window, noting the minimum and average values.

![Screenshot 2023-10-25 122219.png](./screenshot/Screenshot%202023-10-25%20122219.png)

- The minimum value reported is approximately 90.08
- The average value reported is 95.22

These values indicate that the confidence is very high in the polygons for this particular focus area.

**Outcome:** High confidence values indicated that the model was confident in the extracted buildings.

5. Visual inspection of the extraction quality.

![Screenshot 2023-10-25 123202.png](./screenshot/Screenshot%202023-10-25%20123202.png)

6. Observed that some buildings, particularly those surrounded by trees, might be missing from the extraction. After considering the confidence values found in the feature layer, you see that none of the buildings in the trees have been found. This omission is most likely due to the deep learning tool not being confident in the buildings that it found in the trees and discarding them due to the confidence threshold.

**Outcome:** Successfully reviewed the extracted buildings.

**4. Re-extract Building Footprints:**

In this step, I adjusted the model arguments to find additional building footprints that were not extracted in the previous process.

![Screenshot 2023-10-25 123551.png](./screenshot/Screenshot%202023-10-25%20123551.png)

1. In the `History` pane, opened the `Detect Objects Using Deep Learning` tool.
2. Confirmed that the `Input Layer` was set to `AthensTX_2018` and the `Model For Object Detection` used the `Building Footprint Extraction - USA` package.
3. Changed the `Threshold` value from `0.9` to `0.7` to capture more buildings.
4. Set the `Output Name` to `AthensFinalDeepLearning_[initials]` and confirmed the `Building Footprint Focus Area` was selected as the mask.

**Outcome:** The deep learning tool began processing with the adjusted threshold.

![Screenshot 2023-10-25 123949.png](./screenshot/Screenshot%202023-10-25%20123949.png)

5. After processing, I observed the new layer in the `Layers` pane.
6. Dragged the `AthensTestDeepLearning_[initials]` layer above the `AthensFinalDeepLearning_[initials]` layer.
7. Changed the fill color of the `AthensTestDeepLearning_[initials]` layer to green for better visibility.
8. Zoomed into the middle of the focus area to inspect the newly extracted footprints.

![Screenshot 2023-10-25 124836.png](./screenshot/Screenshot%202023-10-25%20124836.png)


**Outcome:** The new building footprints were visible, extracted with the lower confidence threshold.

9. Clicked on one of the blue buildings to review its confidence value.

![Screenshot 2023-10-25 133012.png](./screenshot/Screenshot%202023-10-25%20133012.png)

The confidence value for the selected building is `89.98`. This extracted building was previously not included because the confidence value was below 90. Adjusting the threshold value in the model argument, allowed extracted buildings with a lower confidence value to be included.

If this process was to be used for actual collection of extracted buildings, then the threshold value might be further adjusted to find the optimal threshold.

**Outcome:** Successfully reviewed the results of the re-extraction with the adjusted threshold.

10. Finally, I saved the map and closed the web browser.



## Using ArcGIS Dashboards to Share Imagery Result:  Analyzing Building Footprint Detection in Athens, Texas

I utilized ArcGIS Dashboards to review and share the results of the deep learning analysis focused on building footprint detection in Athens, Texas. This involved using a web map featuring extracted building footprints alongside contextual elements to understand the results and suggest improvements.

![dashboard](./Shared-image-service-dashboard/Screenshot%202023-10-26%20120248.png)

![dashboard](./Shared-image-service-dashboard/Screenshot%202023-10-26%20120309.png)

![dashboard](./Shared-image-service-dashboard/Screenshot%202023-10-26%20120846.png)

![dashboard](./Shared-image-service-dashboard/Screenshot%202023-10-26%20123432.png)


![dashboard](./Shared-image-service-dashboard/Screenshot%202023-10-26%20123632.png)

![dashboard](./Shared-image-service-dashboard/Screenshot%202023-10-26%20124249.png)

**Outcome:**
Shared observations on missing buildings and analyzed confidence levels for extracted buildings.

Noted patterns in detection results, including buildings obscured by trees or unusual roof shapes. Identified potential reasons for missed buildings and observed trends in detection confidence, enhancing overall understanding of the analysis.

**Considering the following themes:**
- Are missing buildings covered by other features?
- Which roof color is missed more often?
- Which roof color is always detected?

* **Observations about the missing buildings.**

Some buildings appear to be partially covered by trees. Others have varied roof forms in one building.

* **Observations about the buildings classified with a confidence value between 70 percent and 80 percent.**

Some buildings appear to be less obscured by trees as the missing buildings or have pixel values spectrally similar to the roads in the imagery layer.

* **Observations about the buildings classified with a confidence value between 80 percent and 90 percent.**

Some buildings appear to be in irregular shapes but have the desired spectral similarities as the other buildings.

The differences that is notice here may not be as obvious, but they are still important to consider. Gathering details about what is causing the lower confidence values will allow to configure the deep learning algorithm more effectively

* **Observations about the buildings classified with a confidence value between 90 percent and 100 percent.**

Some of these buildings are clearly visible in the imagery layer and are easily recognizable.

The building footprints detected with the deep learning package represent a good start to the process of mapping all the buildings in the city. Buildings have been missed, but many have been found.

**4. Next steps**

* **We can consider how to improve the extraction of buildings that were missed in the initial analysis.**

* **Team members can make a copy of the dashboard and add additional elements to improve the data review process.  Adding charts, gauges, or other elements to visualize the data in different ways.**

**Conclusion:**

I demonstrated how to utilize pre-trained deep learning models in ArcGIS Image for ArcGIS Online to extract building footprints from imagery. Improved the extraction results by adjusting model parameters, such as the confidence threshold. This process can be used to efficiently update GIS data, providing valuable information for various applications.

I also demonstrated how to use ArcGIS Dashboards to review and share the results of the deep learning building footprint detection analysis. By exploring the dashboard's interactive features, I gained a better understanding of the model's performance and identified potential areas for improvement. This process highlights the value of dashboards in communicating and analyzing spatial data, enabling informed decisions for urban planning and data management.