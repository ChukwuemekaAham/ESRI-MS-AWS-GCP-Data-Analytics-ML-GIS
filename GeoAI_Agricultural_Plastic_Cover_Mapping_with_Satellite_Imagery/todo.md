# GEE

https://code.earthengine.google.com/6503d98eb855b0e50c317370c8cc24e1 

**It is notable that the training samples we are providing are collected by visually implement of satellite in April and May of each test region.**

Features in the training samples are prepared with images on 20240416 for VNM and Spain and on 20240501 for Kenya.

```javascript

// Load the Kenya Image Collection
var Kenya_IC = ee.ImageCollection("users/pengyuhao/FAO/GEO-AI_2024/Kenya_IC");

// 1. Inspect the Collection
print(Kenya_IC.first()); // View the first image in the collection

// 2. Filter Images by Date
var filteredKenya = Kenya_IC.filterDate('2023-01-01', '2023-12-31'); // Filter for 2023
print(filteredKenya); 

// 3. Calculate a Monthly Composite (Average)
var monthlyKenya = filteredKenya.reduce(ee.Reducer.mean(), ee.Date.fromYMD(2023, 1, 1).advance(1, 'month')); // Start with January 2023
print(monthlyKenya); 

// 4. Display the Composite on the Map
Map.centerObject(Kenya, 7); // Center the map on Kenya
Map.addLayer(monthlyKenya, {bands: ['B4', 'B3', 'B2'], min: 0, max: 3000}, 'Kenya Monthly Composite'); 

// Combine Collections (Assuming they have similar properties)
var all_IC = Kenya_IC.merge(Spain_IC).merge(VNM_IC); 

// Uuse `all_IC` to perform the same analysis as before,
// but across all three countries.

```


```javascript

// Load the Kenya Image Collection
var Kenya_IC = ee.ImageCollection("users/pengyuhao/FAO/GEO-AI_2024/Kenya_IC");

// 1. Inspect the Collection
print(Kenya_IC.first()); // View the first image in the collection

// 2. Filter Images by Date
var filteredKenya = Kenya_IC.filterDate('2023-01-01', '2023-12-31'); // Filter for 2023
print(filteredKenya); 

// 3. Calculate a Monthly Composite (Average)
var monthlyKenya = filteredKenya.reduce(ee.Reducer.mean(), ee.Date.fromYMD(2023, 1, 1).advance(1, 'month')); // Start with January 2023
print(monthlyKenya); 

// Define the point of interest
var point = ee.Geometry.Point([-2.212505629, 36.77824046]); // Replace with your point

// To map a given area with 4 points (defining a polygon), you can use the ee.Geometry.Polygon() function in Google Earth Engine (GEE). 

// Define the 4 points of your area
var point1 = ee.Geometry.Point([-2.212505629, 36.77824046]); 
var point2 = ee.Geometry.Point([-2.5, 37.0]); // Replace with your actual coordinates
var point3 = ee.Geometry.Point([-2.0, 36.5]); // Replace with your actual coordinates
var point4 = ee.Geometry.Point([-2.3, 36.0]); // Replace with your actual coordinates

// Create the polygon from the points
var area = ee.Geometry.Polygon([
  [point1.coordinates().get(0), point1.coordinates().get(1)],
  [point2.coordinates().get(0), point2.coordinates().get(1)],
  [point3.coordinates().get(0), point3.coordinates().get(1)],
  [point4.coordinates().get(0), point4.coordinates().get(1)],
  [point1.coordinates().get(0), point1.coordinates().get(1)] // Close the polygon
]);

// Get the first image
var firstImage = Kenya_IC.first(); 

// Extract values at the point
var extractedValues = firstImage.sampleRegions(point, ['blue_p50', 'green_p50', 'nir_p50', 'nira_p50', 're1_p50', 're2_p50', 're3_p50', 'red_p50', 'swir1_p50', 'swir2_p50', 'VV_p50', 'VH_p50']);

// Calculate 50th percentiles (adjust band names as needed)
var percentiles = extractedValues.reduceColumns(ee.Reducer.percentile([50]), ['blue_p50', 'green_p50', 'nir_p50', 'nira_p50', 're1_p50', 're2_p50', 're3_p50', 'red_p50', 'swir1_p50', 'swir2_p50', 'VV_p50', 'VH_p50']); 

// Add a 'TARGET' column (if needed)
var withTarget = percentiles.map(function(feature) {
  return feature.set('TARGET', 1); // Replace '1' with your target value 
}); 

// Download as CSV
var downloadURL = withTarget.getDownloadURL({format: 'csv'});
print(downloadURL);  // This will print the link for downloading the CSV

```

## Explanation:

- Point of Interest: Define a specific point using its coordinates.
- Extraction: ee.Image.sampleRegions() extracts pixel values at that point.
- Percentiles: ee.Reducer.percentile(50) calculates the 50th percentile for each band.
- Adding a Target: Add a new column to the data using .map().
- Download URL: ee.FeatureCollection.getDownloadURL() generates a link to download the processed data as a CSV.

## Key Points:
- Band Names: The band names in the ee.Image.sampleRegions() call should match the actual band names in the image collection.
- Data Processing: The TARGET column and other processing steps will depend on the specific analysis goals.
