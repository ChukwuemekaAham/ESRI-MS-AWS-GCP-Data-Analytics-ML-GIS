# Observed Meteorology ETL JOB Using xarray and zarr

Goal - Demonstrate my comfort with ETL, xarray, and zarr.

## JUPYTER NOTEBOOK

The code is encapsulated in a Jupyter Notebook file, allowing for interactive execution and exploration of the solution.

## INSTALL PACKAGES

This will install the specified versions of the packages in the Python environment.

```shell
pip install -r requirements.txt
```

## MAIN ETL JOB

see - [meteorology-etl-job](meteorology-etl-job.ipynb)


## ANSWER TO THE QUESTIONS:

**How would you orchestrate this system to run at scale?**

- I would set up an Airflow, Prefect or MageAI DAG (Directed Acyclic Graph) with two main task build_ghcnd_archive (data retieval and upload to durable storage option) and update_ghcnd_archive (data update) to orchestrate the data pipeline. 

- The build_ghcnd_archive task would run once to establish the initial archive, and the update_ghcnd_archive task would run daily through a cron job, to update the archive. 

- I would deploy the Airflow instance on a cloud platform like GCP or AWS and use a Cloud Storage for archives, to take advantage of the scalability and reliability of the cloud infrastructure.

**What major risks would this system face?**

- Data availability and reliability: 

The system relies on data from the NCEI, and any disruptions or changes in the data source could impact the pipeline. Redundancy and monitoring would be crucial to ensure the pipeline continues to function correctly.

- Scaling to handle all >100k GHCND stations: 

As the system needs to scale to handle more stations, the data volume and processing requirements would increase significantly. Careful planning and optimization of the data storage and processing would be necessary to ensure the system can handle the increased load.

- Potential data quality issues: 

The input data from the NCEI might have quality issues or inconsistencies, which could lead to problems in the output archive. Implementing data validation and cleaning steps would be important to maintain the integrity of the archive.

**What are the next set of enhancements you would add?**

- Detect and flag potential data quality issues or anomalies in the archived data.

- Develop a way for users (e.g., the Machine Learning team and customers) to easily access and explore the data in a scalable and reliable storage archive solution that can handle the data archive to include all >100k GHCND stations.

- Keep track of changes and updates to the archive through version control and change tracking, allowing users to access historical versions if necessary.

**How would you improve the clarity of this assignment?**

- Clarify the expected behavior of the update_ghcnd_archive function, especially around handling partial data updates (e.g., what happens if the data for a single day is missing).

- Include correct link to sample data to avoid confusing the candidate.

*****************
