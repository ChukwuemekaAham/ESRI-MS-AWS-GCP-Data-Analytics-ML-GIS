# Rapid Geospatial Analysis of Flood Impacts on Cropland in Maiduguri, Borno State, Nigeria (September 2024)

## Project Overview

This project aims to conduct a rapid geospatial analysis of the flood impacts on cropland in Maiduguri, Borno State, Nigeria, during the September 2024 flood event. The analysis leverages remote sensing data, primarily Sentinel-2 imagery, alongside ESA Landcover data to assess flood extent and crop damage.

**ESA Landcover Data:** This project utilizes the ESA Landcover 100m dataset. This global dataset provides land cover information for various land use types. For this project, we are focusing on Cropland (LC code 40).

But we can also utilize other codes such as:

* Tree Cover (LC code 10)
* Shrubland (LC code 20)
* Grassland (LC code 30)
* Built-up (LC code 50)
* Bare / Sparse Vegetation (LC code 60)
* Mangroves (LC code 90)

This will help in analyzing the specific impacts of the floods on different land cover types and assess the overall vulnerability of the region. 

## Problem Statement

Although flooding is not a recurring issue in Maiduguri, it often cause significant damage to agricultural lands and impacting food security. Understanding the extent and severity of flood-related damage is crucial for effective disaster response, recovery planning, and long-term mitigation efforts.

Area = 810.87 km2

## Research Questions

* **Flood Extent and Severity:**  What was the spatial extent and severity of flooding in Maiduguri in September 2024?
* **Crop Impact Assessment:**  How much cropland were affected by the flood, and what types of landcover types were most impacted?

## Data Sources

* **Sentinel-2:** Sentinel-2 imagery from June 2024 (pre-flood) and August/September 2024 (post-flood) will be used for:
    * Mapping flood extent using a water mask or flood detection algorithm.
    * Calculating the Normalized Difference Vegetation Index (NDVI) to assess crop health and identify flood-affected areas.
* **ESA Landcover Data:**  Downloaded for Maiduguri to identify the types of land cover affected by flooding.

## Pipeline

**1. Data Acquisition:**

* **Download Sentinel-2 Data:** Acquired Sentinel-2 data for June 2024 (pre-flood) and August/September 2024 (post-flood) over Maiduguri. The script uses Google Earth Engine to search for the necessary data and the Data Space Browser to initially visualize the area.
* **Download ESA Landcover Data:**  Downloaded ESA Landcover 100m data for Maiduguri.

**2. Data Processing:**

* **Flood Extent Mapping:**
    * Calculate the Modified Normalized Difference Water Index (MNDWI) for pre-flood (June) and post-flood (August/September) Sentinel-2 images using Earth Engine.
    * Apply a threshold to the MNDWI to create a binary flood mask.
    * Combine the flood masks from both periods to get the overall flood extent.
* **Landcover Processing:**
    *  Use Earth Engine and `geemap` to open the ESA Landcover data.
    *  Clip the Landcover data to the region of interest (`roi`)
    *  Convert the Landcover raster to vector polygons using Earth Engine and `geemap`.

**3. Flood Impact Analysis:**

* **Crop Impact Assessment:**
    * Calculate the NDVI for the pre-flood and post-flood Sentinel-2 images using Earth Engine.
    * Mask the NDVI with the flood extent mask to get NDVI values only for flooded areas.
    * Calculate statistics (e.g., mean NDVI, standard deviation) for the NDVI in the flooded areas.
    *  Compare pre-flood and post-flood NDVI values to assess crop health changes.
    *  Visualize the NDVI in the flooded areas using `geemap` and Earth Engine, highlighting areas of significant NDVI change. 
* **Land Cover Impact Assessment:**
    * Intersect the flood extent with the ESA Landcover layer to identify flooded land cover areas.
    * Calculate the area of each flooded land cover type.
    * Visualize the affected land cover types using `geemap` and Earth Engine. 

**4. Output and Communication:**

* **Report Generation:** Create a comprehensive report with maps, charts, and descriptive text summarizing the findings.
* **Data Sharing:** Share processed data and results (potentially as Zarr or GeoTIFF files) with stakeholders.
* **Communication:** Communicate your findings to relevant stakeholders, such as government agencies, humanitarian organizations, or local communities. 

## Additional Considerations

* **Time Series Analysis:**  Download Sentinel-2 data for multiple dates around the flood to analyze the situation's evolution.
* **Machine Learning:** Explore automated flood extent, crop damage, and vulnerability detection using machine learning algorithms.
* **Community Engagement:** Gather ground-truth data and validate the analysis through community engagement.
* **Uncertainty Assessment:** Analyze uncertainty associated with data sources and analytical methods using bootstrapping or other statistical techniques.