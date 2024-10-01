# Rapid Geospatial Analysis of Flood Impacts buildings and landcover in Maiduguri, Borno State, Nigeria (September 2024)

## Project Overview

This project aims to conduct a rapid geospatial analysis of the flood impacts in Maiduguri, Borno State, Nigeria, during the September 2024 flood event. The analysis leverages remote sensing data, primarily Sentinel-2 imagery, alongside OpenStreetMap data to assess flood extent, buildings affected, crop damage, and the vulnerability of affected populations.

## Problem Statement

Although flooding is not a recurring issue in Maiduguri, it often cause significant damage to agricultural lands and impacting food security. Understanding the extent and severity of flood-related damage is crucial for effective disaster response, recovery planning, and long-term mitigation efforts.

## Research Questions

* **Flood Extent and Severity:**  What was the spatial extent and severity of flooding in Maiduguri in September 2024?
* **Crop Impact Assessment:**  How much cropland and buildings were affected by the flood, and what types of landcover types were most impacted?
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

* **Download Sentinel-2 Data:** Acquired Sentinel-2 data for September 2024 over Maiduguri. The script uses Google Earth Engine to search for the necessary data and the Data Space Browser to initially visualize the area.
* **Download OpenStreetMap Data:**
    * Define a bounding box for Maiduguri using Google Maps or OpenStreetMap's map editor.
    * Use the `osmnx` library to query the OpenStreetMap API and download the buildings information data within the bounding box.

#### Analysis and Visualization:
- The code combines the Sentinel-2 and OpenStreetMap data.
- It calculates the flooded landcover area by intersecting the water mask with the landcover layer.
- It then visualizes the data using Matplotlib. The code creates a flood extent map, a crop impact map showing NDVI, and a vulnerability map using the flooded landcover ratio.

#### Output and Communication
... (Generate report, share data, and communicate findings) ...

**2. Data Processing:**

* **Sentinel-1 Processing:**
    * Sentinel-2 data is processed using googel earth engine ee and geemap to open the downloaded image and extract relevant bands.
    * Apply a water mask (or a flood detection algorithm) using:
        * Existing water mask datasets for the area (e.g., Global Surface Water).
        * Thresholding on a suitable band (e.g., NDWI).
        * Machine learning model trained on known flooded areas.
    * Calculate NDVI using the appropriate bands.
    * Threshold NDVI values to identify healthy and unhealthy vegetation, potentially indicating flood damage.
* **OpenStreetMap Processing:**
    * Load and process the OpenStreetMap data using the `osmium` library to extract building footprints and land use information.
    * Create a GeoDataFrame using `geopandas` for the extracted OpenStreetMap data, including geometries and attributes.
    * Transform the GeoDataFrame to the same coordinate reference system (CRS) as your Sentinel-2 data.

**3. Analysis and Visualization:**

* **Combine Datasets:** Overlay the Sentinel-2 data (NDVI and water mask) with the OpenStreetMap and ESA Landcover data (buildings and land use) using GeoPandas.
* **Calculate Flood Impacts:**  Intersect the water mask with the landcover layer to identify flooded landcover areas.
* **Compute Vulnerability:**
    * Calculate the ratio of flooded landcover to total landcover at different scales (e.g., municipality level).
    * Calculate the number of buildings affected by the flood
    * Use population density data to calculate the exposure of people to flooded landcover (e.g., people per square meter of flooded landcover).
* **Visualization:** Create maps and charts to visualize:
    * Flood extent map in Maiduguri.
    * Crop impact map showing areas of flooded landcover, with severity indicated by color.
    * Vulnerability map displaying exposure of people to flooded landcover using a heatmap.

**4. Output and Communication:**

* **Report Generation:** Create a comprehensive report with maps, charts, and descriptive text summarizing the findings.
* **Data Sharing:** Share processed data and results (potentially as Zarr or GeoTIFF files) with stakeholders.
* **Communication:** Communicate your findings to relevant stakeholders, such as government agencies, humanitarian organizations, or local communities. 

## Additional Considerations

* **Time Series Analysis:** Download Sentinel-2 data for multiple dates around the flood to analyze the situation's evolution.
* **Machine Learning:** Explore automated flood extent, crop damage, and vulnerability detection using machine learning algorithms.
* **Community Engagement:** Gather ground-truth data and validate the analysis through community engagement.
* **Uncertainty Assessment:** Analyze uncertainty associated with data sources and analytical methods using bootstrapping or other statistical techniques.
* **3D Visualization:** Use tools like `pyvista` for immersive 3D visualizations.