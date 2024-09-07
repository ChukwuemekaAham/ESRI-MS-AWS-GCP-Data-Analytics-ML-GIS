# MLOPS GOLD PRICE PREDICTION

## Introduction

Gold price prediction is a critical task for investors, financial analysts, and policymakers due to gold's significance as a hedge against inflation and currency fluctuations. Accurate forecasting of gold prices can lead to more informed decision-making and better risk management. To achieve reliable predictions, we leverage advanced machine learning models and MLOps practices to create a robust, scalable, and automated gold price prediction system.

This project aims to build an end-to-end MLOps pipeline for predicting gold prices. It encompasses data collection, preprocessing, model training, deployment, and monitoring using Azure Machine Learning services. The goal is to ensure that our model remains accurate, reliable, and continuously improving with minimal manual intervention. 

## Technologies Used
- Terraform - as Infrastructure-as-Code (IaC) provide setup aws and gcp services
- MLFlow - for experiment tracking and model registry
- MageAI - for orchestration load, transform, train, inference, export
- EvidentlyAI and Grafana - for monitoring
- GCP Compute Engine - for run mage and run model in cloud
- AWS ECS / - for run mage and run model in cloud
- AWS ECR - for storing registry image or model
- GCP Cloud Storage / AWS S3 - for storing model files