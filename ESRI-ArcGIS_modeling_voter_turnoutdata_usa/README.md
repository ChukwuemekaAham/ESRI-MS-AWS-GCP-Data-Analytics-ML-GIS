# Introduction

Data engineering is a fundamental part of every analysis. The term refers to the planning, preparation, and processing of data to make it more
useful for analysis. It can include simple tasks like identifying and correcting imperfections in your data and calculating new fields. It can also
include more complex tasks like reducing the dimensions of a multivariate dataset.

Data engineering also involves the process of geoenriching your data. Geoenrichment can include various tasks:
· Adding a spatial location to your data, referred to as geocoding
· Using other data sources to extract information and add, or enrich, these values to your dataset
· Calculating new fields that represent spatial characteristics, like the distance from a particular feature in a landscape

In this project, I use ArcGIS Notebooks and the Data Engineering view in ArcGIS Pro to perform data engineering tasks. These tasks use the built-in tools that are available with these products as well as tools that are available by integrating open-source libraries. Using ArcGIS
Notebooks allows you to document and share the steps you take to prepare your data for an analysis. You will then have transparent and
reproducible research or analysis.


## Scenario

Because voting is voluntary in the United States, the level of voter participation (referred to as "voter turnout") has a significant impact on the election results and resulting public policy.

Modeling voter turnout, and understanding where low turnout is prevalent, can inform outreach efforts to increase voter participation. With the ultimate goal of predicting voter turnout, I focus on performing various data engineering tasks to prepare election result data for predictive analysis.

The data for this section is obtained from the Harvard DataverseOpens in new window and the United States Census BureauOpens in new window. The voter turnout dataset from Harvard Dataverse has vote totals from each U.S. county for U.S. presidential elections from 2000 to 2020.

## Requirements

To begin, you will need the ArcGIS Pro with license.

**a.** Start ArcGIS Pro.
**b.** If necessary, sign in with your ArcGIS account.
**c.** Near Recent Projects, click Open Another Project.
Note: If you have configured ArcGIS Pro to start without a project template or with a default project, you will not see the Start page. On the Project tab, click Open, and then click Open Another Project.

![Screenshot 2023-09-03 153307.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-03%20153307.png)


![Screenshot 2023-09-03 153533.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-03%20153533.png)

Rename: DE_Vis.gdb to DataEngineering_and_Visualization.gdb 

**d.** Browse to the DataEngineering_and_Visualization folder that you saved on your computer.
**e.** Click DataEngineering_and_Visualization.aprx to select it, and then click OK.

see: [DataEngineering_and_Visualization](./DataEngineering_and_Visualization/) for project files

see [screenshots](./1%20-%20Perform%20data%20engineering%20tasks/screenshot/)

## Summary
After completing various data engineering techniques, I cleaned and prepared the election data. Geoenabling and geoenriching the data
provides demographic variables that can be used to model or predict voter turnout.

********************************************************************

In [Explore data using visualization techniques](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/), I use various visualization techniques to explore relationships between voter turnout and these variables. This information was used to identify potential variables to use in a prediction model later.


# Introduction

Data visualization helps you digest information by using symbols to visually represent quantities and categories. You can quickly make comparisons
and perceive relative proportions, patterns, relationships, and trends. Data visualization is important throughout the analysis process, from
exploring your data, to interpreting your results, to communicating your findings. Various data visualization techniques are available in ArcGIS. 

I used this various visualization techniques to explore relationships and patterns of voter turnout and to identify potential variables to
use in a predictive analysis.


A Data Visualization map tab gray basemap with a map layer that contains the 2020 election results for counties that have been
enriched with demographic variables. 


![Screenshot 2023-09-03 193042.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-03%20193042.png)


The CountyElections2020 layer has also been projected to the USA Contiguous Equidistant Conic
projected coordinate system. The feature class that created using the Data Engineering Notebook is projected in the WGS84
coordinate system, which is a standard coordinate system for web mapping applications. However, this projection does not preserve areas,
distances, or angles. Because this layer will be used for a distance-based analysis, it was best practice to use an equidistant projection to
preserve true distance measurements on the map.


## Explore fields in the Data Engineering view

First, I explored some of the fields in
the 2020 election results layer using the Data Engineering view to ensure that the data is ready to use in predictive analysis

![Screenshot 2023-09-03 193042.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-03%20193042.png)

Selected four fields to view their statistics to gain a better
understanding of the values and distribution of the fields.

Each row corresponds to a field, and each
column shows a different metric or statistic for each field.

This quick review of my data shows that these fields are not skewed and can be used in the predictive analysis


##  Visualize the data distribution

In this part, I explore the data attributes of the 2020 election results layer and visualize the data distribution.



The histogram visually summarizes the distribution of voter turnout by measuring the frequency at which values appear in the dataset. The
x-axis represents different ranges, or bins, of voter turnout values. The y-axis measures the number of counties with voter turnout values
falling within each range. To learn more about histograms in ArcGIS Pro, go to ArcGIS Pro Help: Histogram.


![Screenshot 2023-09-03 203855.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-03%20203855.png)

The Chart Properties pane includes a list of statistics summarizing the Voter_Turnout_2020 variable. The mean county voter turnout value is
about 0.66, with county values ranging from approximately 0.21 to approximately 1.

********************************

Using these overlays, you can see that the histogram has a fairly symmetrical bell shape with nearly
identical mean and median values. This outcome indicates that the Voter_Turnout_2020 variable is normally distributed. In a normal
distribution, the mean, median, and mode values are equal. This outcome means that most values fall near the average in the center of the
distribution, with fewer and fewer values appearing as you move farther from the center into the left and right tails.

**********************************

The counties with the lowest voter turnout are selected in the histogram, map, and table.

![Screenshot 2023-09-05 093111.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-05%20093111.png)


The counties with the highest voter turnout are selected in the histogram, map, and table.

![Screenshot 2023-09-05 093354.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-05%20093354.png)



*****************************************


### Change layer symbology

Graduated Colors classifies the data into different ranges based on the values of a specified attribute field. Each class is assigned a shade of
color to show the relative difference between the feature values. To learn more about graduated color symbology, go to ArcGIS Pro
Help: Graduated colors.


Natural Breaks (Jenks) is the default classification method because it is data driven. That means the symbol ranges are calculated based on
the data values, making it adaptable to different types of data distributions. Because you have determined that the voter turnout variable is
normally distributed, you will use the Standard Deviation method to classify voter turnout. To learn more about data classification methods,
go to ArcGIS Pro Help: Data classification methods

![Screenshot 2023-09-05 095858.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-05%20095858.png)

By applying a Graduated Colors symbology, you created what is commonly referred to as a choropleth, or thematic, map. Choropleth maps
visualize low-to-high values using light-to-dark colors. Because you are using the Standard Deviation classification method, you applied a
diverging color scheme. A diverging color scheme classifies values based on how far they are from the average. On the Histogram tab, you
can see how the distribution of values corresponds to the classes of color. The counties with below-average voter turnout are represented
in shades of purple, and the counties with above-average voter turnout are represented in shades of green.

![Screenshot 2023-09-05 100149.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-05%20100149.png)

*****************************************

After combining the Graduated Colors symbology with the state layer overlay, one can begin to get a sense of how states compare to each
other in terms of voter turnout. States like West Virginia (WV), Tennessee (TN), and Arkansas (AR) stand out as having low voter turnout, and
states like Colorado (CO), Minnesota (MN), and Wisconsin (WI) stand out as having high voter turnout.

*******************************************


### Visualize data as a bar chart

![Screenshot 2023-09-05 101215.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-05%20101215.png)

The bar chart summarizes county voter turnout values by state. Each bar represents a state, and the height of the bar corresponds to the
mean voter turnout value. For more information about bar charts, go to ArcGIS Pro Help: Bar chart.

Sorting the bars by value makes it easier to visually rank the states from highest to lowest voter turnout.
**************************************************

![Screenshot 2023-09-05 101455.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-05%20101455.png)

West Virginia, Arkansas, and Oklahoma have the lowest county average voter turnout for 2020, which confirms what was observed in the
map. 

The bar chart summarizes the voter turnout for each state into a single average value. Within each state, however, there can be quite a
bit of variation in voter turnout. To examine the individual county voter turnout within each state, I use a filtered bar chart.


![Screenshot 2023-09-05 102748.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-05%20102748.png)


![Screenshot 2023-09-05 102709.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-05%20102709.png)


The county bar chart shows the individual county values within Georgia. Each bar in the county bar chart corresponds to a
single feature on the map, so the colors of the bars match the map symbology.


![Screenshot 2023-09-05 102755](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-05%20102755.png)

![Screenshot 2023-09-05 104127.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-05%20104127.png)

Guides ensures that we reference or highlight significant values or thresholds in our charts



###  Create a box plot

To visualize and compare the distribution of voter turnout values in CountyElections2020 layer for every state at one time, a box plot created with the following parameters:

· Numeric Fields - Voter_Turnout_2020
· Category - State_Name
· Show Outliers - box.

Box plots are automatically sorted alphabetically by their categories (x-axis ascending). The box plot chart allows one to visualize and compare the entire distribution of county voter turnout values for each state.

![Screenshot 2023-09-05 105616.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-05%20105616.png)


Box plots split numeric values into four equal quartiles, and they visualize five key statistics for each distribution: minimum, first quartile,
median, third quartile, and maximum. 

The whiskers extending from the boxes span from the minimum value to the maximum value,
illustrating the full range of values found in each state. The boxes span from the first quartile to the third quartile, illustrating the range of the
middle half of values, or the interquartile range (IQR). The IQR indicates the size of spread, or variability, in voter turnout values in each state.

For more information about box plots, go to ArcGIS Pro Help: Box plot.

![Screenshot 2023-09-05 105808.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-05%20105808.png)

The ToolTip displays the key voter turnout statistics for the state. 

*************************************************

Texas overall has a relatively low voter turnout average. However, there is a
wide range of county voter turnout values, spanning from approximately 0.38 to approximately 1. The counties with voter turnout values
that are very different from the state average are considered outliers and are displayed as dots beyond the plot's whiskers.

**************************************************

![Screenshot 2023-09-05 110054.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-05%20110054.png)

The outliers are selected on the map.

Reviewing the overall distribution of voter turnout values in conjunction with individual feature locations enables one to understand the data
and identify areas that I may want to further investigate.


###  Explore variable relationships in a scatterplot matrix

Because I want to predict voter turnout, I explored the relationship between voter turnout and other variables in my data by creating a scatterplot matrix (data visualization tool) for the CountyElections2020 layer.

- Numeric Fields:
· Voter_Turnout_2016
· Voter_Turnout_2020
· 2022 Median Age
· 2022 Per Capita Income

- Matrix Layout - Histograms

A scatterplot matrix is a grid of scatterplots, also referred to as mini-plots, used to visualize bivariate relationships between combinations of
variables. Each scatterplot in the matrix visualizes the relationship between a pair of variables, allowing many relationships to be explored in
one chart. 

A histogram visualizing the distribution of each individual variable can also be included in the matrix. For more information about
scatterplot matrices, see ArcGIS Pro Help: Scatter plot matrix.

![Screenshot 2023-09-05 112121.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-05%20112121.png)

A linear trend line is added to each scatterplot in the matrix. The direction of the trend line indicates whether the variables have a positive or
negative relationship, and the R-squared (R2) value indicates the strength of the relationship. For more information about scatterplots, go to
ArcGIS Pro Help: Scatter plot.

![Screenshot 2023-09-05 112134.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-05%20112134.png)


****************************************

The mini-plots in the matrix are visualized with a color gradient that corresponds to the strength of the R-squared value. While every pairwise combination of variables is plotted
in the matrix, I am specifically interested in how each variable relates to voter turnout. The column of mini-plots on the far left includes
the relationships between voter turnout and the other variables.

![Screenshot 2023-09-05 112456](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-05%20112456.png)

mini-plot that compares Voter_Turnout_2020 and 2022 Median Age

Median age has a positive relationship with voter turnout, where a higher median age corresponds to a higher voter turnout. However, the
R-squared value for this trend is 0.2, which means that median age alone can explain only about 20 percent of the variability in the voter
turnout value

**********************************


![Screenshot 2023-09-05 112455.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-05%20112455.png)

mini-plot that compares Voter_Turnout_2020 and 2022 Per Capita.

Per capita income also has a positive relationship with voter turnout, where a higher per capita income corresponds to a higher voter
turnout. The R-squared value for this trend is 0.32, which means that per capita income can explain about 32 percent of the variability in
voter turnout values. Within the preview plot, you can see where some of the points deviate from the trend. 

###  Explore relationships at different scales


To investigate whether the strength of the variable relationships varies from place to place, we can filter the scatterplot matrix to include
only counties that are visible on the map by clicking the Filter By Extent button

![Screenshot 2023-09-05 113613.png](./2%20-%20Explore%20data%20using%20data%20visualization%20techniques/screenshot/Screenshot%202023-09-05%20113613.png)


Note: The R-squared values vary based on the size of the map and chart views.


The chart updates to calculate the relationships between the variables of the counties that are visible in the map extent. Comparing the
R-squared values at a national scale to this local scale, we can see that the relationships between voter turnout and per capita income have
increased. However, the relationship between voter turnout and median age has decreased.

*****************************************************

The changes in R-squared values indicate that the linear relationships between the variables vary spatially. We can explore and quantify different types of local relationships by using the Local Bivariate Relationships tool.

******************************************************

Based on the information derived using this tool, the scale of my analysis (for example, county versus state) impact which variables are relevant for a prediction analysis

******************************************************