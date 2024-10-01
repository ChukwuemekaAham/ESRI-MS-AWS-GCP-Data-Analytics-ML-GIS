# A rapid geospatial analysis of the flood impacts on crops in KwaZulu-Natal province of South Africa in 2022 - MODIFY TO MAIDUGRI BORNO NIGERIA FLOOD SEPTEMBER 06, 2024

## URI
https://openknowledge.fao.org/handle/20.500.14283/cc1046en

## Synopsis (short abstract)
South Africa is the southern most country on the African continent with the 121 309 ha of land area and highly dependent on agriculture sector (79 percent of agricultural land area) for food, income, and employment. Natural disasters like drought, floods, storms, cyclones etc. causes significant socio-economic damages and losses, as well as negatively impacting the agricultural sector. From 11–13 April 2022, heavy rainfall caused severe flooding and landslides affecting the south and south-eastern part of South Africa. Particularly, in the Provinces of KwaZulu-Natal and Eastern Cape, authorities reported loss of lives, infrastructure damages and inundated cropland. Disaster Charter 755 was activated for South Africa. From 19–20 April, moderate rainfall waa forecast over north-eastern South Africa, while no heavy rainfall was expected over the already affected Provinces. In this context, the Food and Agriculture Organization of the United Nations (FAO) Geospatial Unit of the Land and Water Division (NSL) with support from SFS REOSA conducted a rapid geospatial assessment on crops and the exposure of rural people during the period 10–20 April 2022. This assessment provides information at the district, local municipalities and ward levels in the area of interest (AOI). This analysis combines Sentinel 1 (S1) Synthetic Aperture Radar (SAR) and Sentinel 2 (S2) imagery (both at a 10 m spatial resolution) with Planet imagery (5 m spatial resolution) and 2020 population data from Worldpop (100 m spatial resolution) to determine: (1) flood extent; (2) cropland area; (3) flooded crop area; and (4) exposure of population to flooded cropland. The results are provided in the form of maps by administrative units and tabular with descriptive statistics for the aforementioned indicators. With recent advances in geospatial and information technologies and updated land cover maps, crop specific information adapted to national conditions with tailored field campaigns have the potential to better support response programmes and agricultural development in the future. The key findings from this rapid assessment are that for Area of Interest (AOI): 1) total flooded area in the Province of Eastern Cape is 373 868 ha and in the Province of KwaZulu-Natal is 137 601 ha; 2) total cropland area estimated in Area of Interest is 1 386 941 ha; 3) overall inundated cropland is 51 601 ha (4 percent of the total land in AOI); and 4) the most affected districts in respect to people exposure to floods are Cacadu (54 616).

## Keywords

flooding, flood damage, impact assessment, rural population, displacement, farmland, infrastructure, spatial analysis, spatial data, South Africa

# Rapid Geospatial Analysis of Flood Impacts on Crops in Maiduguri, Borno State, Nigeria (September 2024)

## Project Overview

This project aims to conduct a rapid geospatial analysis of the flood impacts on crops in Maiduguri, Borno State, Nigeria, during the September 2024 flood event. The analysis leverages remote sensing data, primarily Sentinel-2 imagery, alongside OpenStreetMap data to assess flood extent, crop damage, and the vulnerability of affected populations.

## Problem Statement

Flooding is a recurring issue in Maiduguri, often causing significant damage to agricultural lands and impacting food security. Understanding the extent and severity of flood-related crop damage is crucial for effective disaster response, recovery planning, and long-term mitigation efforts.

## Research Questions

* **Flood Extent and Severity:**  What was the spatial extent and severity of flooding in Maiduguri in September 2024?
* **Crop Impact Assessment:**  How much cropland was affected by the flood, and what types of crops were most impacted?
* **Vulnerability Assessment:** What are the most vulnerable areas and populations in Maiduguri with respect to flood-related crop damage, considering factors such as population density and crop type distribution?

## Data Sources

* **Sentinel-2:** Sentinel-2 imagery from September 2024 will be used for:
    * Mapping flood extent using a water mask or flood detection algorithm.
    * Calculating the Normalized Difference Vegetation Index (NDVI) to assess crop health and identify flood-affected areas.
* **OpenStreetMap Data:** Downloaded for Maiduguri to obtain:
    * Building footprint to determine population density and vulnerability.
    * Land use information (cropland, forest, urban areas) to assess the types of crops impacted by flooding.
* **Population Data:** High-resolution population density data for Maiduguri, potentially from WorldPop or UNOSAT, to assess people's exposure to flooded cropland.

## Pipeline

**1. Data Acquisition:**

* **Download Sentinel-2 Data:** Use the `pystac` library to search and download Sentinel-2 data for September 2024 over Maiduguri via the STAC API (e.g., using the Data Space Browser).
* **Download OpenStreetMap Data:**
    * Define a bounding box for Maiduguri using Google Maps or OpenStreetMap's map editor.
    * Use the `overpy` library to query the OpenStreetMap API and download the PBF data within your bounding box.

**2. Data Processing:**

* **Sentinel-1 Processing:**
    * Read the Sentinel-1 images using `rasterio`.
    * Convert the data to an `xarray` Dataset for analysis.
    * Apply a water mask (or a flood detection algorithm) using:
        * Existing water mask datasets for the area (e.g., Global Surface Water).
        * Thresholding on a suitable band (e.g., NDWI).
        * Machine learning model trained on known flooded areas.
    * Calculate NDVI using the appropriate bands.
    * Threshold NDVI values to identify healthy and unhealthy vegetation, potentially indicating flood damage.
* **OpenStreetMap Processing:**
    * Load and process the OpenStreetMap PBF data using the `osmium` library to extract building footprints and land use information.
    * Create a GeoDataFrame using `geopandas` for the extracted OpenStreetMap data, including geometries and attributes.
    * Transform the GeoDataFrame to the same coordinate reference system (CRS) as your Sentinel-2 data.

**3. Analysis and Visualization:**

* **Combine Datasets:** Overlay the Sentinel-2 data (NDVI and water mask) with the OpenStreetMap data (buildings and land use) using GeoPandas.
* **Calculate Flood Impacts:**  Intersect the water mask with the cropland layer to identify flooded cropland areas.
* **Compute Vulnerability:**
    * Calculate the ratio of flooded cropland to total cropland at different scales (e.g., municipality level).
    * Use population density data to calculate the exposure of people to flooded cropland (e.g., people per square meter of flooded cropland).
* **Visualization:** Create maps and charts to visualize:
    * Flood extent map in Maiduguri.
    * Crop impact map showing areas of flooded cropland, with severity indicated by color.
    * Vulnerability map displaying exposure of people to flooded cropland using a heatmap.

**4. Output and Communication:**

* **Report Generation:** Create a comprehensive report with maps, charts, and descriptive text summarizing the findings.
* **Data Sharing:** Share processed data and results (potentially as Zarr or GeoTIFF files) with stakeholders.
* **Communication:** Communicate your findings to relevant stakeholders, such as government agencies, humanitarian organizations, or local communities. 

## Additional Ideas and Considerations

* **Time Series Analysis:** Download Sentinel-2 data for multiple dates around the flood to analyze the situation's evolution.
* **Machine Learning:** Explore automated flood extent, crop damage, and vulnerability detection using machine learning algorithms.
* **Community Engagement:** Gather ground-truth data and validate the analysis through community engagement.
* **Uncertainty Assessment:** Analyze uncertainty associated with data sources and analytical methods using bootstrapping or other statistical techniques.
* **3D Visualization:** Use tools like `pyvista` for immersive 3D visualizations.

This detailed breakdown outlines a comprehensive geospatial project and pipeline for analyzing the flood impacts on crops in Maiduguri. Adapt the implementation and analysis techniques to match your data availability and project goals.



****************************************************************


For flood mapping in Borno, **Sentinel-1** is generally considered a better choice than Sentinel-2 due to the following reasons:

* **Sentinel-1:**
    * **SAR (Synthetic Aperture Radar):**  Sentinel-1 carries SAR sensors, which can penetrate clouds and see through vegetation. This is crucial for flood mapping in Borno, as the region often experiences cloud cover and dense vegetation.
    * **Water Penetration:**  SAR signals can also penetrate water to some extent, allowing you to detect flooded areas even if the water is relatively deep.
    * **Day and Night Imaging:**  SAR can acquire images day or night, making it suitable for flood monitoring regardless of weather conditions.

* **Sentinel-2:**
    * **Optical Imaging:** Sentinel-2 uses optical sensors, which rely on reflected light. This makes it less effective in cloudy or heavily vegetated areas.
    * **Limited Water Penetration:**  Optical sensors have difficulty penetrating water, so they can only detect flooded areas with shallow water and clear water surfaces.

**Key Advantages of Sentinel-1 for Flood Mapping in Borno:**

* **Cloud Cover:**  The ability to see through clouds is essential in Borno, which experiences a lot of cloud cover.
* **Vegetation:** SAR can penetrate vegetation, allowing you to map flooded areas under dense vegetation.
* **Nighttime Data:**  SAR can provide flood information even during nighttime hours, which is important for tracking floods that occur quickly.

**How to Use Sentinel-1 Data for Flood Mapping:**

* **SAR Processing:** SAR images require specialized processing techniques to generate flood maps. Tools like SNAP (Sentinel Application Platform) and GDAL (Geospatial Data Abstraction Library) are commonly used.
* **Flood Detection Algorithms:** Several algorithms can be used to detect floods from SAR data, such as:
    * **Change Detection:** Comparing images before and after a flood event.
    * **Water Index Algorithms:**  Using specific indices to identify water bodies based on SAR backscatter properties.
    * **Machine Learning:**  Training machine learning models to identify flooded areas.

**Keep in Mind:**

* **Data Availability:**  Sentinel-1 data is freely available from the Copernicus Open Access Hub ([https://scihub.copernicus.eu/](https://scihub.copernicus.eu/)).
* **Processing Expertise:** You'll likely need some expertise in SAR image processing to effectively analyze and generate flood maps from Sentinel-1 data.


# PRODUCT INFO

{"type":"Polygon","coordinates":[[[13.162994,12.039321],[13.040771,11.761159],[13.378601,11.422149],[13.537903,11.583633],[13.241272,11.800146],[13.473358,12.023203],[13.318176,12.141376],[13.162994,12.039321]]]}

1951.23 km2

*****************************************************************

# SENTINEL 2

ATTRIBUTES
Summary
Name:
S2A_MSIL2A_20240823T093031_N0511_R136_T32PRT_20240823T155251.SAFE
Size:
1154MB
Sensing time:
2024-08-23T09:30:31.024000Z
Platform short name:
SENTINEL-2
Instrument short name:
MSI
Product
Absolute orbit number:
47895
Acquisition mode:
INS-NOBS
Beginning date time:
2024-08-23T09:30:31.024000Z
Cloud cover:
21.515934
datastripId:
S2A_OPER_MSI_L2A_DS_2APS_20240823T155251_S20240823T093912_N05.11
Ending date time:
2024-08-23T09:30:31.024000Z
granuleIdentifier:
S2A_OPER_MSI_L2A_TL_2APS_20240823T155251_A047895_T32PRT_N05.11
Modification date:
2024-08-23T17:03:37.792384Z
Origin date:
2024-08-23T16:52:58.000000Z
Processed by:
ESA
Processing date:
2024-08-23T15:52:51.000000+00:00
Processing level:
S2MSI2A
Processor version:
05.11
Product group id:
GS2A_20240823T093031_047895_N05.11
Product type:
S2MSI2A
Publication date:
2024-08-23T17:02:33.541833Z
Relative orbit number:
136
S3Path:
/eodata/Sentinel-2/MSI/L2A/2024/08/23/S2A_MSIL2A_20240823T093031_N0511_R136_T32PRT_20240823T155251.SAFE
sourceProduct:
S2A_OPER_MSI_L2A_TL_2APS_20240823T155251_A047895_T32PRT_N05.11,S2A_OPER_MSI_L2A_DS_2APS_20240823T155251_S20240823T093912_N05.11
sourceProductOriginDate:
2024-08-23T16:52:58Z,2024-08-23T16:52:25Z
Tile id:
32PRT
Instrument
Instrument short name:
MSI
Platform
Platform short name:
SENTINEL-2
Satellite platform:
A
Download single files
S2A_MSIL2A_20240823T093031_N0511_R136_T32PRT_20240823T155251.SAFE
DATASTRIP
DS_2APS_20240823T155251_S20240823T093912
GRANULE
L2A_T32PRT_A047895_20240823T093912
HTML
banner_1.png
banner_2.png
banner_3.png
star_bg.jpg
UserProduct_index.html
UserProduct_index.xsl
rep_info
S2_PDI_Level-2A_Datastrip_Metadata.xsd
S2_PDI_Level-2A_Tile_Metadata.xsd
S2_User_Product_Level-2A_Metadata.xsd
INSPIRE.xml
manifest.safe
MTD_MSIL2A.xml
S2A_MSIL2A_20240823T093031_N0511_R136_T32PRT_20240823T155251-ql.jpg

https://link.dataspace.copernicus.eu/yy5i

https://link.dataspace.copernicus.eu/frm9

https://zipper.dataspace.copernicus.eu/odata/v1/Products(d498a775-41cb-4df5-be2d-568941ab47df)/$value

******************************************************************
# SENTINEL 1

ATTRIBUTES
Summary
Name:
S1A_IW_GRDH_1SDV_20240905T045604_20240905T045629_055525_06C676_00E9.SAFE
Size:
1616MB
Sensing time:
2024-09-05T04:56:04.797959Z
Platform short name:
SENTINEL-1
Instrument short name:
SAR
Product
Absolute orbit number:
55525
Acquisition mode:
IW
Beam id:
IW
Beginning date time:
2024-09-05T04:56:04.797959Z
Completion time from ascending node:
2805240
Cycle number:
331
Data take id:
444022
Ending date time:
2024-09-05T04:56:29.796001Z
Instrument configuration id:
7
Modification date:
2024-09-05T07:01:19.107472Z
Orbit direction:
DESCENDING
Origin date:
2024-09-05T06:53:49.388000Z
Polarisation:
VV&VH
Processed by:
ESA
Processing center:
Production Service-SERCO
Processing date:
2024-09-05T06:41:08.181466+00:00
Processing level:
LEVEL1
Processor name:
Sentinel-1 IPF
Processor version:
003.80
Product class:
S
Product composition:
Slice
Product type:
IW_GRDH_1S
Publication date:
2024-09-05T07:01:01.902180Z
Relative orbit number:
153
S3Path:
/eodata/Sentinel-1/SAR/IW_GRDH_1S/2024/09/05/S1A_IW_GRDH_1SDV_20240905T045604_20240905T045629_055525_06C676_00E9.SAFE
Segment start time:
2024-09-05T04:55:11.097000+00:00
Slice number:
3
Slice product flag:
false
Start time from ascending node:
2780242
Timeliness:
Fast-24h
Total slices:
6
Instrument
Instrument short name:
SAR
Platform
Platform short name:
SENTINEL-1
Satellite platform:
A

Download single files

Download single files
S1A_IW_GRDH_1SDV_20240905T045604_20240905T045629_055525_06C676_00E9.SAFE
annotation
calibration
rfi
s1a-iw-grd-vh-20240905t045604-20240905t045629-055525-06c676-002.xml
s1a-iw-grd-vv-20240905t045604-20240905t045629-055525-06c676-001.xml
measurement
s1a-iw-grd-vh-20240905t045604-20240905t045629-055525-06c676-002.tiff
s1a-iw-grd-vv-20240905t045604-20240905t045629-055525-06c676-001.tiff
preview
icons
map-overlay.kml
product-preview.html
quick-look.png
thumbnail.png
support
s1-level-1-calibration.xsd
s1-level-1-measurement.xsd
s1-level-1-noise.xsd
s1-level-1-product.xsd
s1-level-1-quicklook.xsd
s1-level-1-rfi.xsd
s1-map-overlay.xsd
s1-object-types.xsd
s1-product-preview.xsd
manifest.safe
S1A_IW_GRDH_1SDV_20240905T045604_20240905T045629_055525_06C676_00E9.SAFE-report-20240905T065131.pdf

https://zipper.dataspace.copernicus.eu/odata/v1/Products(043dad6f-c0be-409d-9639-200b54d696f9)/$value

**********************************************************************