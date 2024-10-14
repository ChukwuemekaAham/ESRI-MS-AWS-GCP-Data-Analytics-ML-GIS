##  Predictive Modeling for Voter Turnout Using ArcGIS Pro

Prediction is an important part of spatial data science. You can use prediction to forecast future values.

This project uses ArcGIS Pro's deep learning capabilities to create a predictive model for voter turnout in the United States.  The goal is to use existing data to predict voter turnout at a smaller scale (census tracts), informing a "Get Out the Vote" canvassing campaign to target regions with low turnout.

## Scenario

After preparing and visualizing the data, it was used in predictive analysis for creating a models that predict voter turnout. These
models used explanatory variables, such as income and age, to predict the dependent variable, which is voter turnout.

The model was used to downscale voter turnout from the county level to the census tract level. The information was used to organize a "Get Out the
Vote" canvassing campaign. These campaigns encourage people to vote on Election Day. The model helped to identify local regions that are expected to have low voter turnout so that one knows where to target the campaign.

The Forest-based Classification and Regression tool which uses an adaptation of Leo Breiman's random forest algorithm (a supervised machine learning algorithm) were used to train and evaluate the predictive model, modifying variables and parameters to improve the model performance.

The tool creates many decision trees, called an ensemble or a forest, that are used for prediction. Each tree generates its own prediction and is used as part
of a voting scheme to make final predictions. 

The strength of the forest-based method is in capturing commonalities of weak predictors (the trees) and combining them to create a powerful predictor (the forest). 

## Requirements

**a.** Start ArcGIS Pro.
**b.** Near Recent Projects, click Open Another Project.
Note: If you have configured ArcGIS Pro to start without a project template or with a default project, you will not see the Start page. On the Project tab, click Open, and then click Open Another Project.
**c.** Browse to the Prediction folder that you saved on your computer.

![Screenshot 2023-09-06 204911.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-06%20204911.png) 

**e.**  Click Prediction.aprx to select it, and then click OK

see: [Prediction](./Prediction/) for project files

The Prediction map tab opens to a gray basemap with a map layer that represents the 2020 election results for each county in the United States.

Counties with a voter turnout value below the mean are purple, and counties with a voter turnout value above the mean are green.


## Create a prediction model

During the data engineering process, the election data were enriched with various demographic variables. The data was then visualized, to explore the relationship of these variables to voter turnout, identifying variables that have a strong relationship to voter
turnout. These variables were used in the first prediction model.

**Creating a prediction model using the Forest-based Classification and Regression tool**

![Screenshot 2023-09-06 211533.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-06%20211533.png)

The following parameters were used:

· Prediction Type: Train Only
· Input Training Features: CountyElections2020
· Variable To Predict: Voter_Turnout_2020
- Explanatory Training Variables:
· 2022 Median Age
· 2022 Per Capita Income
· 2022 Pop Age 25+: High School/No Diploma: Percent

Additional:
· Output Trained Features: Out_Trained_Features
· Output Variable Importance Table: Out_Variable_Importance_Table

![Screenshot 2023-09-07 115830.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-07%20115830.png)


**reviewing the initial model's performance metric**

![Screenshot 2023-09-07 121714.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-07%20121714.png)

By default, forest-based classification and regression reserves 10 percent of the data for validation. The model is trained without this random subset, and the tool returns an R-squared value that measures how well the model performed on the unseen data.

When a model is evaluated based on the training dataset rather than a validation dataset, it is common for estimates of performance to be overstated due to a concept called overfitting. Therefore, the validation R-squared value is a better indicator of model performance than the training R-squared
value. 

The model returned a validation R-squared value of 0.529, indicating that the model predicted the voter turnout value in the validation dataset with an accuracy of about 53 percent.


**reviewing how important each explanatory variable was in generating a prediction** 

The Out_Trained_Features layer displays the predicted voter
turnout for each county in the contiguous United States. The variable importance table and associated bar chart are used to explore which variables were most important in this prediction.

![Screenshot 2023-09-08 112724.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-08%20112724.png)

The **2022 Per Capita Income** and **2022 Pop Age 25+: High School/No Diploma: Percent** variables have the highest importance, meaning that they were the most useful in predicting voter turnout.

As previously mentioned, each time that you run the Forest-based Classification and Regression tool, you may get slightly different results due to the
randomness introduced in the algorithm. To understand and account for this variability, you will use a parameter that allows the tool to create
multiple models in one run. This output will allow you to explore the distribution of model performance.

To learn more about the Forest-based Classification and Regression (Spatial Statistics) tool, go to ArcGIS Pro Help: Forest-based Classification and
Regression (Spatial Statistics).


**4. Examine Model Stability:**
* Reviewed the prediction intervals in the model to see whether the model's performance is relatively stable across all values using the `Forest-based Classification And Regression` tool.

![Screenshot 2023-09-06 211533.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-06%20211607.png)

![Screenshot 2023-09-07 120812.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-07%20120812.png)

* `Validation Data: Regression Diagnostics`.
    ![Screenshot 2023-09-07 120812.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-07%20121714.png)
    - **Outcome:** The validation R-squared values for the 10 runs vary slightly due to the randomness in the algorithm. The tool trained 10 models with random subsets of validation data. From the above, the most representative R-squared value across the 10 runs is 0.529, corresponding to about 52 percent accuracy in prediction of the validation data. A histogram was also used to review the distribution of R-squared values returned over the 10 runs

* `Validation R2` chart.
    ![Validation R2_2.png](./Create%20a%20prediction%20model/screenshot/img/Validation%20R2_2.png)
    - **Outcome:** The histogram shows the variability in model performance by visualizing the distribution of R-squared values returned over the 10 runs. The mean R-squared value for the 10 runs of this model is 0.529.


* `Distribution Of Variable Importance` chart.
    ![Distribution of Variable Importance_2.png](./Create%20a%20prediction%20model/screenshot/img/Distribution%20of%20Variable%20Importance_2.png)
    - **Outcome:** Instead of a bar chart, the variable importance is visualized using a box plot to show the distribution of importance across the 10 runs of the model. In some runs of the model, Per Capita Income was more important, and in other runs, Pop Age 25+: High School/No Diploma: Percent was also important. Overall, both variables are strong candidates for your predictive model

* `Prediction Interval` chart.
    ![Prediction Interval_2.png](./Create%20a%20prediction%20model/screenshot/img/Prediction%20Interval_2.png)
    - **Outcome:** The Prediction Interval chart displays the level of uncertainty for any given prediction value. By considering the range of prediction values returned by
    the individual trees in the forest, prediction intervals are generated, indicating the range in which the true value is expected to fall. You can be 90
    percent confident that new prediction values generated using the same explanatory variables would fall in this range. This chart can help you identify
    whether the model is better at predicting some values than others. For example, if the confidence intervals were much larger for low voter turnout
    values, then you would know that the model is not as stable for predicting low voter turnout as it is for predicting high voter turnout. The prediction
    intervals in this model are fairly consistent, indicating that the model performance is relatively stable across all values.


**5. Add Many Variables to a Prediction Model:**

The Forest-based Classification and Regression tool uses a random subset of the available explanatory variables in each decision tree.
Commonalities in the predictions and variables used among all the trees in the forest are quantified in the variable importance diagnostic. In general,
that means that you can test adding variables to the model without diminishing the model's predictive power. Variables that are useful result in
higher variable importance scores, and variables that are not useful result in lower variable importance scores.

* Adding more Explanatory Training Variables:
    * `Pop_Sqmi`
    * `State_Abbr`
    * `Voter_Turnout_2008`
    * `Voter_Turnout_2012`
    * `Voter_Turnout_2016`
    * `2022 Value Of Checking/Savings/Money Mkt/CDs: Average`
    * `2021 HHs: Inc Below Poverty Level (ACS 5-Yr): Percent`
    * `2022 Pop Age 25+: Bachelor's Degree: Percent`
    * `2022 Average Disposable Income`
    * `2022 Cash Gifts To Political Orgs: Average`
    * `2022 Pop Age 15+: Never Married: Percent`
    * `2022 Pop Age 25+: GED: Percent`
    * `2022 Value Of Credit Card Debt: Average`
    * `2022 Pop Age 25+: High School Diploma: Percent`
    * `2022 Pop Age 25+: Grad/Professional Degree: Percent`
    * `2022 Pop Age 25+: < 9th Grade: Percent`
    * `2022 Average Household Income`
    * `2022 Dominant LifeMode Grp Code`

Many variables are now added as explanatory training variables. Voter turnout for 2020 is the variable that you are trying to understand, and the
same variable should not be used as both the independent and dependent variables for this analysis. The Forest-based Classification and Regression
tool can also use categorical variables, which are variables of a string field type instead of a numeric field type. The State_Abbr and the 2022
Dominant LifeMode Grp Code variables are both marked as categorical variables in the Explanatory Training Variables list

* Reviewing the R-squared value in the validation data regression diagnostics again

* `Validation R2` chart.
    ![Validation R2_3.png](./Create%20a%20prediction%20model/screenshot/img/Validation%20R2_3.png)
    - **Outcome:** The histogram shows the variability in model performance by visualizing the distribution of R-squared values returned over the 10 runs. The mean R-squared value for the 10 runs of this model is 0.529.


*  `Validation Data: Regression Diagnostics` section showing the R-squared values for the 10 runs after adding additional variables.
    ![Screenshot 2023-09-08 122911.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-08%20122911.png)
    - **Outcome:** The R-squared value will increase due to the inclusion of additional explanatory variables. the model's R-squared value increased to 0.896, which means that it is now predicting with almost 89 percent accuracy based on the
    validation data. 
    
    The warning that shows in the tool message window is because the State_Abbr categorical variable contains more
    than 15 categories. 
    
    The more categories that a variable contains, the more likely it is that the variable will dominate the model and lead to less
    effective prediction results. This is something to consider, when selecting variables for the model.

* `Distribution Of Variable Importance` 
    ![Distribution of Variable Importance_3.png](./Create%20a%20prediction%20model/screenshot/img/Distribution%20of%20Variable%20Importance_3.png)
    - **Outcome:** The voter turnout variables have the highest variable importance in the model, but several new variables have contributed to the model and raised its
    performance. There are also several variables that may not be helping the model, represented by their low variable importance.
    With the Forest-based Classification and Regression tool, you can also calculate new variables based on distances to meaningful locations. In the next
    step, you will calculate distance variables and assess their importance to the model.

**6. Add Distance Variables to the Model:**
You want to incorporate each county's urban and rural characteristics into the model to determine whether these variables improve voter turnout
predictions. To represent urban and rural characteristics, you will calculate the distance between each county and cities of various sizes. The proximity to each of these cities will be used to represent the urban and rural characteristics, with more rural counties being farther from cities.

* Using the `DistanceVariables` group layer, the following six distance variables 
    * `Cities10`
    * `Cities9`
    * `Cities8`
    * `Cities7`
    * `Cities6`
    * `Cities5`

were created by draging the selected layers into the Geoprocessing pane, under Explanatory Training Distance Features and used in training the model.

![Screenshot 2023-09-08 132714.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-08%20132714.png) 

* `Out_Trained_Features`.
When a city point is contained within a county, the distance will be zero.
![Screenshot 2023-09-08 140946.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-08%20140946.png) 


The Forest-based Classification and Regression tool calculates the distances from each county to the nearest city of each class (the closest class 5 city,
the closest class 6 city, and so on). These distances are added to the Out_Trained_Features layer as separate attribute fields.


* Review the R-squared value and `Distribution Of Variable Importance` chart in the tool message window.

* `Validation Data: Regression Diagnostics`
    ![Screenshot 2023-09-08 141742.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-08%20141742.png)
    - **Outcome:** The R-squared value will increase as you include distance variables. In this example, the model's R-squared value increased to 0.883, which means that it is predicting with about 88 percent accuracy based on the
    validation data. 

* `Distribution Of Variable Importance` chart after adding distance variables 
    ![Distribution of Variable Importance_4.png](./Create%20a%20prediction%20model/screenshot/img/Distribution%20of%20Variable%20Importance_4.png)
    - **Outcome:** The chart will show the importance of distance variables compared to other factors. The distance to Cities7 and the distance to the largest cities (Cities10) are more important than the other distance variables. Overall, however, these
    variables were not as helpful as the income and voter turnout variables.
    Identifying a "good" model is subjective and varies greatly based on the industry and how the model will be used. In many fields, including many of
    the social sciences, an R-squared value that is greater than 0.70 might be considered satisfactory for making a prediction. Before using this model to
    predict, you will simplify the model to include only the most important variables.
    

**7. Refine the Model:**

Refining your model is typically an iterative process, where you remove some variables and then rerun and evaluate the model. There are many
different ways to select variables to include in a model. In this analysis, the most important variables are chosen by defining a threshold in the variable
importance table. In this step, you will refine the model to only include the variables with variable importance above the selected threshold

* The following `Explanatory Training Variables` were removed:
    * `2022 Value Of Checking/Savings/Money Mkt/CDs: Average`
    * `2022 Pop Age 25+: Bachelor's Degree: Percent`
    * `2022 Average Disposable Income`
    * `2022 Cash Gifts To Political Orgs: Average`
    * `2022 Pop Age 25+: GED: Percent`
    * `2022 Value Of Credit Card Debt: Average`
    * `2022 Pop Age 25+: High School Diploma: Percent`
    * `2022 Pop Age 25+: Grad/Professional Degree: Percent`
    * `2022 Pop Age 25+: < 9th Grade: Percent`
    * `2022 Average Household Income`
    * `2022 Dominant LifeMode Grp Code`
    * `all distance variables under`

* Setting the `Number Of Trees` to `1000` the model training was carried out again. 

Increasing the number of trees improves the chance that each variable will be used in a decision tree, resulting in a more accurate model prediction.
Specifying the number of trees is a balance between the accuracy of the model and the processing time to generate the model


* Review:

    ![Screenshot 2023-09-08 145035.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-08%20145035.png)

* `validation R-squared value` 
    - **Outcome:** If the R-squared value is approximately 0.980, the model predicted voter turnout in the validation data with an accuracy of about 98 percent.

* `mean R-squared value over the 10 runs of this model`
    - **Outcome:**  The chart should show the distribution of R-squared values from the 10 runs. If the R-squared values for each run of the model range from about 0.81 to 0.91, thenthe mean value is approximately 0.89.
 

* `Two most important explanatory variables in this model`
    ![Screenshot 2023-09-08 145018.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-08%20145018.png)
    - **Outcome:** The two most important variables are Voter_Turnout_2016 and Voter_Turnout_2012.

The simplified model has a higher R-squared value, meaning that removing the variables with low importance did not compromise model
performance and enhanced the model's performance

**8. Examine Additional Model Metrics:**

review additional model metrics to help you assess whether the model requires any additional changes.

* `Model Out Of Bag Errors`

![Screenshot 2023-09-08 150553.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-08%20150553.png)

Model Out Of Bag Errors is another diagnostic that can help validate the model. The percentage of variation explained indicates the percentage of
variability in voter turnout that can be explained using this model. Model Out Of Bag Errors also shows how much performance is gained by
increasing the number of trees in the model. If the percentage of variation explained significantly increases from the 500 to the 1000 column, you
may want to increase the number of trees to improve model performance.
This model does not see a significant increase in percentage of variation explained, so you do not need to increase the number of trees. Remember:
due to the randomness built into algorithms, varied results are expected.

* `Explanatory Variable Range Diagnostics`
![Screenshot 2023-09-08 150705.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-08%20150705.png)

The Explanatory Variable Range Diagnostics section lists the range of values covered by each explanatory variable in the datasets that are used to
train and validate the model. 

For example, median age values spanned from 22 to 64 in the dataset that is used to train the model and from 26 to 60 in the dataset that is used to validate the model.

The Share column indicates the percentage of overlap between the values that are used to train and the values that are used to validate. In this
example, 80 percent of the median age values that are used to train the model were used to validate the model.

A value that is greater than 1
indicates that the model predicted values outside the range of values in the training data. To minimize extrapolation, you will review this diagnostic as
you predict voter turnout for census tracts.

**9. Predict Values:**

You trained a model using the county data that you had available. You can use this model to predict voter turnout at the census tract level, which is
much higher resolution and will allow you to get a sense of more detailed spatial patterns.
To predict voter turnout at the tract level, you need census tract data with explanatory variables that match the explanatory variables that are used to
train the model. In this step, you will train the model using the county data and then apply that model to the same variables at the tract level to
predict voter turnout

* Parameters:
    * Prediction Type: Predict To Features.
    * Input Prediction Features: `Tracts`.
    * Output Predicted Features: Type `Out_Predicted_Features`.

    * Match Explanatory Variables for `Prediction`:  
    ![Screenshot 2023-09-08 182134.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-08%20182134.png)

For the purpose of this analysis, using 2019 variables is acceptable because the difference between 2019 values and 2021 or 2022 values is minimal.

The `Training Data Excluded For Validation`, is set to `10 percent`
.
By removing the voter turnout variables, you changed the model. Because of this change, you will leave Training Data Excluded For Validation as 10 percent so you can assess model performance at the Tract level. If the variables had remained the same, you no longer need to assess the model's
performance and you could change this parameter to 0 to use all the training data to train the model so that the model can predict to the best of its
ability.

**Outcome:** The model was applied to the census tract data, generating predictions for voter turnout at the tract level. 

* `Prediction`
    ![Screenshot 2023-09-08 184931.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-08%20184931.png)

    ![Screenshot 2023-09-08 183505.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-08%20183505.png)


* `Model Out Of Bag Errors`
    ![Screenshot 2023-09-08 183550.png](./Create%20a%20prediction%20model/screenshot/Screenshot%202023-09-08%20183550.png)
    - **Outcome:** The percentage of variation explained was reduced, but it does not vary greatly between 500 trees and 1,000 trees. Because it does not vary much between 500 and 1000, there is no need to run the model again with more trees.

* `Prediction Interval` chart for `Out_Predicted_Features` 
    ![Prediction Interval_3.png](./Create%20a%20prediction%20model/screenshot/img/Prediction%20Interval_3.png)
    **Outcome:**

### Summary

The wide confidence intervals show that the model does not perform as well at the tract level as it did at the county level. In particular, it may be
prone to overestimating turnout for low-turnout tracts. Because the goal of the analysis is to identify areas with low voter turnout, this model is not
reliable enough to meet the needs.

When we change the scale of our analysis, we need to change or update the model. In this scenario, votes in the United States are mostly
calculated at the county level and are not calculated at the tract level. The tract-level prediction does not work nationwide. The factors that
drive voter turnout are likely very different from place to place, making it difficult to find a model that predicts well for the entire country. 

It is often a good practice to reduce the study area and create more localized models. 