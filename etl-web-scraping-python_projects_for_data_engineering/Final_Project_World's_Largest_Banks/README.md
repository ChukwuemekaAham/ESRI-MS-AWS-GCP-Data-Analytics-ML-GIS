# Final project; Acquiring and Processing Information on the World's Largest Banks 

## Overview

In this project, I worked on real-world data and perform the operations of Extraction, Transformation, and Loading as required.

## Project Scenario
You have been hired as a data engineer by research organization. Your boss has asked you to create a code that can be used to compile the list of the top 10 largest banks in the world ranked by market capitalization in billion USD. Further, the data needs to be transformed and stored in GBP, EUR and INR as well, in accordance with the exchange rate information that has been made available to you as a CSV file. The processed information table is to be saved locally in a CSV format and as a database table.

- Your job is to create an automated system to generate this information so that the same can be executed in every financial quarter to prepare the report.

Parameter - Value
- Code name	- banks_project.py
- Data URL	- https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks
- Exchange rate CSV path	- https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv
- Table Attributes (upon Extraction only)	- Name, MC_USD_Billion
- Table Attributes (final)	- Name, MC_USD_Billion, MC_GBP_Billion, MC_EUR_Billion, MC_INR_Billion
- Output CSV Path	- ./Largest_banks_data.csv
- Database name	- Banks.db
- Table name	- Largest_banks
- Log file	- code_log.txt

## Directions
- Write a function to extract the tabular information from the given URL under the heading By Market Capitalization, and save it to a data frame.
- Write a function to transform the data frame by adding columns for Market Capitalization in GBP, EUR, and INR, rounded to 2 decimal places, based on the exchange rate information shared as a CSV file.
- Write a function to load the transformed data frame to an output CSV file.
- Write a function to load the transformed data frame to an SQL database server as a table.
- Write a function to run queries on the database table.
- Run the following queries on the database table:
a. Extract the information for the London office, that is Name and MC_GBP_Billion
b. Extract the information for the Berlin office, that is Name and MC_EUR_Billion
c. Extract the information for New Delhi office, that is Name and MC_INR_Billion
- Write a function to log the progress of the code.
- While executing the data initialization commands and function calls, maintain appropriate log entries.


```python

# Code for ETL operations on Country-GDP data
# Importing the required libraries
def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''

def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''
    return df

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''
    return df

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''
''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''


df['MC_GBP_Billion'] = [np.round(x*exchange_rate['GBP'],2) for x in df['MC_USD_Billion']]

#Quiz question prompt:
Experiment with the statement provided for adding the transformed columns to the dataframe. There will be a question on this in the quiz.

Print the contents of df['MC_EUR_Billion'][4], which is the market capitalization of the 5th largest bank in billion EUR. Note this value, as it will be the answer to a question in the final quiz.

Print the contents of the entire table
Query statement:

SELECT * FROM Largest_banks

Print the average market capitalization of all the banks in Billion USD.
Query statement:

SELECT AVG(MC_GBP_Billion) FROM Largest_banks

Print only the names of the top 5 banks
Query statement:

SELECT Name from Largest_banks LIMIT 5

```