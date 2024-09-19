# Restaurant Revenue End-to-End Data Pipeline

## About Dataset
The Restaurant Revenue Prediction Dataset is a comprehensive collection of simulated data designed for predicting monthly revenue for a set of fictitious restaurants. This dataset was created for educational and illustrative purposes, allowing data enthusiasts to explore and experiment with machine learning algorithms for regression tasks.

`datasource:` https://www.kaggle.com/datasets/mrsimple07/restaurants-revenue-prediction

`run cells:` [restaurant_elt_analysis.ipynb](restaurant_elt_analysis.ipynb) in Microsoft Fabric Synapse Data Engineering Workspace, to create Dimensions Tables and Fact Table

## Switch to SQL Analytics 
Run queries to create views and queries

```sql
-- Create a View for Cuisine Type Dimension Save as vDimCuisineType
SELECT 
    CuisineTypeID = ROW_NUMBER() OVER (ORDER BY Cuisine_Type), Cuisine_Type
FROM
    (
        SELECT DISTINCT Cuisine_Type 
        FROM sales_raw
    ) AS DimCuisineType

-- Create a View for Promotion Dimension Save as vPromotionName
SELECT DISTINCT Promotion AS Promotion 
CASE
    WHEN Promotion = 0 THEN 'No Promotion'
    WHEN Promotion = 1 THEN 'Promotion'
    ELSE 'unknown'
END AS PromotionName
FROM sales_raw

-- Create a View for the FactTable Save as vFactRestaurant
select Number_of_Customers,	Menu_Price,	Marketing_Spend,	Average_Customer_Spending,	Promotions,	Reviews,	Monthly_Revenue,b.CuisineTypeID from sales_raw a
left join DimCuisineType b
on a.Cuisine_Type = b.Cuisine_Type
```


## Create New Semantic Model in Lakehouse
- Select Dimensions and Fact Tables and Create relationships

`View:`

- Calculation groups
- Cultures
- Relationships
- Create measures
- Perspectives
- Roles
- Tables

![factTable](./img/Screenshot%202024-09-19%20131250.png)

## Create New PowerBI Report

- Fact by cuisine type, sum, value label (CHART)
- Customer spend, sum, value label(CHART)
- Total spend as a value
- Menu price sum
- Average menu price

## REPORT: 

`scan:` [restaurant revenue report.jpg](restaurant%20revenue%20report.jpg) to visit report


![restaurant revenue report.png](./img/Screenshot%202024-09-19%20141415.png)

![restaurant revenue report.png](./img/Screenshot%202024-09-19%20142327.png)