# Accessing Databases using Python Script


Using databases is an important and useful method of sharing information. To preserve repeated storage of the same files containing the required data, it is a good practice to save the said data on a database on a server and access the required subset of information using database management systems.

In this lab, you'll learn how to create a database, load data from a CSV file as a table, and then run queries on the data using Python.

## Objectives

Create a database using Python

Load the data from a CSV file as a table to the database

Run basic "queries" on the database to access the information

## Scenario
Consider a dataset of employee records that is available with an HR team in a CSV file. As a Data Engineer, you are required to create the database called STAFF and load the contents of the CSV file as a table called INSTRUCTORS. The headers of the available data are :

- Header	Description
- ID	Employee ID
- FNAME	First Name
- LNAME	Last Name
- CITY	City of residence
- CCODE	Country code (2 letters)

Practice Problems

### In the same database STAFF, create another table called Departments. The attributes of the table are as shown below.

- Header	Description
- DEPT_ID	Department ID
- DEP_NAME	Department Name
- MANAGER_ID	Manager ID
- LOC_ID	Location ID

Populate the Departments table with the data available in the Departments CSV file.

### Append the Departments table with the following information.

- Attribute	Value
- DEPT_ID	9
- DEP_NAME	Quality Assurance
- MANAGER_ID	30010
- LOC_ID	L0010

Run the following queries on the Departments Table:
a. View all entries
b. View only the department names
c. Count the total entries