# MLOPS GOLD PRICE PREDICTION

## Introduction

Gold, a timeless symbol of wealth and a haven during economic storms, plays a crucial role in the global financial landscape. As a hedge against inflation and currency fluctuations, understanding its price trends is vital for investors, financial analysts, and policymakers alike. Accurate gold price prediction can empower informed decision-making and enhance risk management.

This project takes a comprehensive approach to gold close price forecasting, leveraging the power of machine learning and MLOps practices. The goal is to build a robust, scalable, and automated system that delivers reliable predictions with minimal manual intervention.

## The MLOps pipeline encompasses the following key stages:

- Data Collection: Gathering of historical gold price data along with relevant economic indicators from reliable sources.
- Data Preprocessing: This crucial step involves cleaning, transforming, and preparing the collected data for model training.
- Model Training: Utilizing machine learning models. Training a robust model capable of predicting future gold prices.
- Deployment: Trained model will be deployed using AWS, GCP, Streamlit, Containers, ensuring accessibility and scalability for users.
- Monitoring: Continuous monitoring of the model's performance and the underlying data will ensure accuracy and reliability, facilitating ongoing model improvement.

By automating this entire pipeline, I aim to achieve a gold price prediction system that remains accurate, reliable, and continuously evolving to adapt to market dynamics. 

## Technologies Used

- Terraform - as Infrastructure-as-Code (IaC) provide setup aws and gcp services
- MLFlow - for experiment tracking and model registry
- MageAI - for orchestration load, transform, train, inference, export
- EvidentlyAI and Grafana - for monitoring
- GCP Compute Engine - for run mage and run model in cloud
- AWS ECS / - for run mage and run model in cloud
- AWS ECR - for storing registry image or model
- GCP Cloud Storage / AWS S3 - for storing model files
- PostgreSQL Database
- Sqlite Database
- Github actions for CI-CD