# The Medallion Architecture: A Data Cleaning Framework for Microsoft Fabric

The Medallion Architecture is a versatile data cleaning framework that complements existing data organization approaches in a lakehouse environment. This framework ensures compatibility and adaptability while promoting data quality and consistency, allowing businesses to leverage its benefits alongside their current data models.

## Understanding the Layers

**Bronze (Raw) Layer:** The initial landing zone for all data, regardless of its structure (structured, semi-structured, or unstructured). Data remains in its original format, untouched.

**Silver (Validated) Layer:** This layer focuses on data refinement and validation. Activities include merging and combining data, removing nulls, and deduplicating records. This layer serves as a consistent data repository accessible to various teams within an organization.

**Gold (Enriched) Layer:** Data in the gold layer undergoes further refinement to meet specific business and analytical needs. This could involve aggregation, external data enrichment, or other transformations. This layer prepares data for downstream consumption by analytics, data science, and MLOps teams.

## Project Goal

This project explored the potential of implementing the Medallion Architecture design within Microsoft Fabric. The goal was to effectively organize and transform Sales Order (2019, 2020, and 2021) data across the Bronze, Silver, and Gold layers of a lakehouse, optimizing the data for analytics.

## Key Benefits of the Medallion Architecture:

* **Flexibility:**  The architecture seamlessly integrates with existing data models, allowing customization.
* **Data Quality:**  Ensures data consistency and quality by implementing validation rules across layers.
* **Scalability:**  Supports handling large datasets and diverse data sources within the lakehouse environment.
* **Adaptability:**  Provides a flexible framework to handle the ever-changing needs of data landscapes.

This project showcases how the Medallion Architecture can be a powerful tool for data cleaning and transformation within Microsoft Fabric, improving data analytics capabilities.

# Objectives
- Apply the medallion architecture framework within the Microsoft Fabric environment.
- Analyze 2019, 2020, and 2021 orders datasets stored in lakehouse using DirectLake in Power BI.

# Prerequisites
- Microsoft Fabric lakehouses
- Apache Spark, and 
- SparkSQL.

# Result

![factTable](./img/Screenshot%202024-09-18%20193134.png)

![lineage](./img/Screenshot%202024-09-19%20213937.png)

## REPORT: 

`scan:` [sales gold report.jpg](./medallion_sales_gold_report.jpg) to visit report

`link:` https://app.fabric.microsoft.com/links/Ltf3ZMtujS?ctid=dc49a365-cfe1-43b9-9c3f-61dc19c8f7e2&pbi_source=linkShare

![sales gold report.png](./img/Screenshot%202024-09-19%20220634.png)