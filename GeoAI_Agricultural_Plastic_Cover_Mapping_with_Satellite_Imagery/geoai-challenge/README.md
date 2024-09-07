## GeoAI Agricultural Plastic Cover Mapping with Satellite Imagery

### Project Overview

This project aims to develop accurate and cost-effective classification models for agricultural plastic cover using freely available satellite datasets. The goal is to advance the mission of global agricultural plastic cover mapping using remote sensing data.

### Data and Files

* **raw-data:** Contains the original CSV files for training and testing.
  - `Kenya_training.csv`: Training data for Kenya, including target values.
  - `Kenya_testing.csv`: Testing data for Kenya, without target values.
  - `Spain_training.csv`: Training data for Spain, including target values.
  - `Spain_validation.csv`: Testing data for Spain, without target values.
  - `VNM_training.csv`: Training data for Vietnam, including target values.
  - `VNM_testing.csv`: Testing data for Vietnam, without target values.
  - `VariableDefinitions.csv`: Description of each variable in the datasets.

* **cleaned-data:**  Will contain cleaned versions of the training datasets (e.g., `kenya_training_cleaned.csv`).

* **notebooks:**  Contains Jupyter notebooks for analysis and model development.

### Instructions

```
C:.
│   manifest-9ed045dadc98edf1fd0a80f83f7676f520240708-24674-10td86v.json
│   methodology.md
│   notes.md
│   README.md
│   todo.md
│   
└───geoai-challenge
    │   notes.md
    │   README.md
    │   requirements.txt
    │   SampleSubmission.csv
    │
    ├───cleaned-data
    ├───notebooks
    │   │   kenya_analysis.ipynb
    │   │   spain_analysis.ipynb
    │   │   vietnam_analysis.ipynb
    │   │
    │   └───log
    │           kenya_log.txt
    │
    └───raw-data
            Kenya_testing.csv
            Kenya_training.csv
            Spain_training.csv
            Spain_validation.csv
            VariableDefinitions.csv
            VNM_testing.csv
            VNM_training.csv

```

1. **Set up folders:** Create the folders outlined in the "geoai-challenge" project setup section above.
2. **Download data:** Download the CSV files from the link provided and place them in the `raw-data` folder.

###  Environment

- **Python Version:** 3.9 or higher
- **Required Libraries:**
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn 
  - mlflow
  - joblib
  - streamlit

### Requirements.txt

3. **run:** pip install -r requirements.txt

```
geoai-challenge/
    ├── raw-data
    ├── cleaned-data
    └── notebooks
         ├── kenya_analysis.ipynb
         ├── spain_analysis.ipynb
         └── vietnam_analysis.ipynb

```

4. **Run the notebook:** Open each `country_analysis.ipynb` notebook and run the code cells sequentially. The notebook will perform exploratory data analysis, visualize data, and save cleaned datasets. 


### Hardware

- Local machine with Jupyter Notebook installed

### Expected Run Time

- Exploratory data analysis (EDA): time in minutes (unknown for now)
- Model training and evaluation (using MLflow):  time in minutes  (unknown for now)

### Notes

- This README will be updated with more details and instructions as the project progresses.