# Extract, Transfrom and Load GDP Data Project

## Introduction
In this project, I created a complete ETL pipeline for accessing data from a website and processing it to meet the requirements.

## Project Scenario:
An international firm that is looking to expand its business in different countries across the world has recruited you. You have been hired as a junior Data Engineer and are tasked with creating an automated script that can extract the list of all countries in order of their GDPs in billion USDs (rounded to 2 decimal places), as logged by the International Monetary Fund (IMF). Since IMF releases this evaluation twice a year, this code will be used by the organization to extract the information as it is updated.

**The required data seems to be available on the URL mentioned below:**

'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'

The required information needs to be made accessible as a `CSV` file `Countries_by_GDP.csv` as well as a table `Countries_by_GDP` in a database file `World_Economies.db` with attributes `Country` and `GDP_USD_billion`.

Your boss wants you to demonstrate the success of this code by running a query on the database table to display only the entries with more than a 100 billion USD economy. Also, you should log in a file with the entire process of execution named `etl_project_log.txt`.

You must create a Python code 'etl_project_gdp.py' that performs all the required tasks.

## Objectives

- Write a data extraction function to retrieve the relevant information from the required URL.

- Transform the available GDP information into 'Billion USD' from 'Million USD'.

- Load the transformed information to the required CSV file and as a database file.

- Run the required query on the database.

- Log the progress of the code with appropriate timestamps.


```python

# Code for ETL operations on Country-GDP data

# Importing the required libraries

def extract(url, table_attribs):
    ''' This function extracts the required
    information from the website and saves it to a dataframe. The
    function returns the dataframe for further processing. '''

    return df

def transform(df):
    ''' This function converts the GDP information from Currency
    format to float value, transforms the information of GDP from
    USD (Millions) to USD (Billions) rounding to 2 decimal places.
    The function returns the transformed dataframe.'''

    return df

def load_to_csv(df, csv_path):
    ''' This function saves the final dataframe as a `CSV` file 
    in the provided path. Function returns nothing.'''

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final dataframe as a database table
    with the provided name. Function returns nothing.'''

def run_query(query_statement, sql_connection):
    ''' This function runs the stated query on the database table and
    prints the output on the terminal. Function returns nothing. '''

def log_progress(message):
    ''' This function logs the mentioned message at a given stage of the code execution to a log file. Function returns nothing'''

''' Here, you define the required entities and call the relevant 
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''

```