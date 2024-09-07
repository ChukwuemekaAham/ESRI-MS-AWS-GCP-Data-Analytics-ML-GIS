# GeoAI Agricultural Plastic Cover Mapping with Satellite Imagery

## Can you map plastic covering using satellite imagery?

https://zindi.africa/onboarding
https://zindi.africa/competitions

## Description

The global use of plastics in agriculture is increasing due to the expansion of intensive and semi-intensive agricultural practices aimed at enhancing crop yields, such as the application of covering materials for fields, orchards, and greenhouses. These agricultural plastics are predominantly derived from synthetic petrochemical polymers and are often contaminated with pesticides and fertilizers. Consequently, they are becoming a significant environmental concern, necessitating proper collection and disposal at the end of their useful life. The monitoring of plastic-covered is essential for the sustainable development of horticulture. This practice supports high-quality agricultural production in limited areas, enhances cost-effectiveness, and reduces pollution.

Satellite observations can be utilized for identifying agricultural plastic covers on regional to global scales. A variety of methodologies, including indices methods and machine learning algorithms at both pixel and object levels, have been proposed for this purpose. These methodologies employ multi-source remote sensing datasets, ranging from low-resolution MODIS imagery to high-resolution WorldView and QuickBird image series, as well as radar data, as inputs for plastic cover mapping. However, due to the complexity of plastic materials used in agricultural applications, there is currently no available global map detailing the spatial distribution of agricultural plastic covers, and extending existing methodologies to larger scales remains a significant challenge.

To address these challenges and advance the mission of global agricultural plastic cover mapping using remote sensing data, a new initiative has been launched to develop accurate and cost-effective classification models for agricultural plastic cover using freely available satellite datasets. By participating in this challenge, researchers and practitioners can contribute to the advancement of global cropland mapping, enabling a more precise and comprehensive understanding of agricultural landscapes worldwide.

## About AI for Good - International Telecommunication Union (ITU)


AI for Good is organized by ITU in partnership with 40 UN Sister Agencies. The goal of AI for Good is to identify practical applications of AI to advance the United Nations Sustainable Development Goals and scale those solutions for global impact. It’s the leading action-oriented, global & inclusive United Nations platform on AI.

## Evaluation
The error metric for this competition is Accuracy.

For every row in the dataset, submission files should contain 2 columns: ID and Target.

Your submission file should look like this:

ID              TARGET 
Kenya_1  	  1
Kenya_2  	  0
Prizes
1st prize: 500 CHF

2nd prize: 300 CHF

3rd prize: 200 CHF

There are 3 000 Zindi points available. You can read more about Zindi points here.

## Timeline
Competition closes on 11 November 2024.

Final submissions must be received by 11:59 PM GMT.

We reserve the right to update the contest timeline if necessary.


## About
Participants should use all free-accessible satellite data (e.g. Landsat, Sentienl-1/2) in the test regions, the data pre-processing methodology are not limited, either. We will provide the example GEE JS scripts in code editor to generate 15-day composited Sentinel-2 time series data in the three test regions (Spain, Kenya and Vietimn). The participants need to share the availability of the data they used and how the pre-processing is conducted, if they used more data than the official provided data set.

We will provide a limited number of training samples for plastic cover mapping, participants can also collect some training samples by themselves as cropland extent can be visually interpreted from Google Earth and Satellite images. It is notable that the training samples we are providing are collected by visually implement of satellite in April and May of each test region.

If you are in the top 10 at the end of the challenge and receive the request for code email you must include the following:

1. The bi-weekly spatial distribution of the agricultural plastic covers in all the three test regions during 2023
2. Executable and technical document describing the algorithm and procedure.
3. Training samples with the features used for the classification procedure. We will provide training samples, and the participants could add training samples by themselves.
4. Code used for data processing.

## Note: 
we will evaluate the potential of the submitted code for data processing according to the technical document (from the RAW data to the resulting maps); the submission will not be accepted if the methodology is evaluated as unrepeatable. The submitted script is limited to python and Google Earth Engine JavaScript.

## The satellite data are available by GEE with following script.

var Kenya_IC = ee.ImageCollection("users/pengyuhao/FAO/GEO-AI_2024/Kenya_IC")
var Spain_IC = ee.ImageCollection("users/pengyuhao/FAO/GEO-AI_2024/Spain_IC")
var VNM_IC = ee.ImageCollection("users/pengyuhao/FAO/GEO-AI_2024/VNM_IC")
Features in the training samples are prepared with images on 20240416 for VNM and Spain and on 20240501 for Kenya.

# Files

DESCRIPTION - FILES

This file describes the variables found in train and test.
VariableDefinitions.csv
1.8 KB

Train contains the target. This is the dataset that you will use to train your model.
VNM_training.csv
103.4 KB

Train contains the target. This is the dataset that you will use to train your model.
Spain_training.csv
90.3 KB

Test resembles Train.csv but without the target-related columns. This is the dataset on which you will apply your model to.
Spain_validation.csv
87.8 KB

Test resembles Train.csv but without the target-related columns. This is the dataset on which you will apply your model to.
VNM_testing.csv
102.6 KB

Test resembles Train.csv but without the target-related columns. This is the dataset on which you will apply your model to.
Kenya_testing.csv
103.4 KB

Train contains the target. This is the dataset that you will use to train your model.
Kenya_training.csv
104.8 KB

Is an example of what your submission file should look like. The order of the rows does not matter, but the names of the "ID" must be correct.
SampleSubmission.csv
28.2 KB


# Reproducibility of submitted code
If your submitted code does not reproduce your score on the leaderboard, we reserve the right to adjust your rank to the score generated by the code you submitted.
If your code does not run you will be dropped from the top 10. Please make sure your code runs before submitting your solution.
Always set the seed. Rerunning your model should always place you at the same position on the leaderboard. When running your solution, if randomness shifts you down the leaderboard we reserve the right to adjust your rank to the closest score that your submission reproduces.
Custom packages in your submission notebook will not be accepted.
You may only use tools available to everyone i.e. no paid services or free trials that require a credit card.

# Datasets and packages

- The solution must use publicly-available, open-source packages only.

- If the challenge is a computer vision challenge, image metadata (Image size, aspect ratio, pixel count, etc) may not be used in your submission.

- You may use only the datasets provided for this competition. Automated machine learning tools such as automl are not permitted.

- You may use pretrained models as long as they are openly available to everyone.

- You are allowed to access, use and share competition data for any commercial,. non-commercial, research or education purposes, under a CC-BY SA 4.0 license.

- You must notify Zindi immediately upon learning of any unauthorised transmission of or unauthorised access to the competition data, and work with Zindi to rectify any unauthorised transmission or access.

- Your solution must not infringe the rights of any third party and you must be legally entitled to assign ownership of all rights of copyright in and to the winning solution code to Zindi.

# Documentation
A README markdown file is required

**It should cover:**

- How to set up folders and where each file is saved
- Order in which to run code
- Explanations of features used
- Environment for the code to be run (conda environment.yml file or an environment.txt file)
- Hardware needed (e.g. Google Colab or the specifications of your local machine)
- Expected run time for each notebook. This will be useful to the review team for time and resource allocation.