1. Get all the archhives
2. Put them in their respective country folders
3. State requirements in requirements.txt file
    - Use python virtual environment and piplock file
    - Install imports
6. Create .ipynb project directory
7. State the Goal and Objectives
8. Declare Imports
9. Declare Variables
10. Use modular programming in notebook
11. Import data
12. Hold each data in their individual dataframes
13. Perform EDA and Feature Engineering
    - Visualize the data
    - Set indexes
    - Set types
    - Point Counts
    - Transform the data as required
    - Pay close attention to their Median as it is an imagery analysis (describe)
    - Check for outliers
    - Clean the data (missing, null, wrong shape)
    - Remove unrequired
    - Visualize (Correlation and Scatter Plotting)
    - Look for relevant features
    - Merge data by country
    - Create Cleaned Data
    - Create ML Data with Enrinched Columns and Tag Column - VALIDATE, TRAIN, TEST
28. Start model training
    - Choose a model that is suitable for training the data, based on EDA Keynotes
    - Use the Cleaned Data Directory
    - Split the dataset (80% for training, 10% each for Validation and Testing) - use pd.query to split by tags
    - Check MSE and R2 (BASE on STATS During EDA, Make your deductions on the performance and predictions)
    - MLFlow for tracking and Experiment
    - Write predictions to a file
    - Submit predictions and R2
