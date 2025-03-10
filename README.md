# Running Dashboard

## Purpose of the project
This web application creates a dashboard of running statistics and trends from exported Strava and Apple Health data. By pairng these two datasets together, this app intends to help runners view their performance statistics and progress overtime. The race pace predictor is also a useful tool for runners to view their estimated performance on race days based off their current traninng efforts, and can therefore make adjustments to their training plan.

App initially ran on render: https://running-dashboard.onrender.com/
Aiming to migrate this on vercel for less server issues.

![Untitled design (3)](https://github.com/Raine0554/running-dashboard/assets/96808637/9366c3af-9605-4380-b978-21909c6f699e)

Here's a screenshot

<img width="1454" alt="Screenshot 2024-07-09 at 8 51 37 pm" src="https://github.com/Raine0554/running-dashboard/assets/96808637/401b6a20-129c-47c7-8128-d90b4642bd45">


## Why I made this application
As a beginner runner, I find Strava a really useful app for analysing individual runs, but noticed that it lacked features for tracking training distributions and progress over time. I wanted to see how my pace has improved throughout my training. Additionally, I wanted to predict my race performance in October by applying a linear regression model to my current progression trends.

I also integrated my Apple health data to analyse other running performance indicators such as max heart rate and VO2 max. A decreasing max heart rate and an increase VO2 max are good signs of improving fitness levels. 

Lastly, tracking my energy expenditure trends throughout the week would help me ensure I get adequate nutrition intake, avoiding issues such as over- or under-fuelling.

## Documents
Here are the different files in the project:

* Strava and Health Exploratory Data Analysis: A Jupyter Notebook that details the data preprocessing and visualisation for the project.
* Race Performance Estimator: A Jupyter Notebook that details my whole process for constructing a linear regression model.
* [Data Visualization:](https://github.com/Raine0554/running-dashboard/blob/main/app.py) The python code I did for visualizing the data and creating the dashboard application.

## Library Requirements 
* pandas
* dash
* plotly
* scikit learn
* numpy

## How to use this application
The link to the dashboard sources its data from my own local csv files that I exported from the Strava and Apple Health apps. Here's what you can do if you'd like to use this dashboard for your own data:

1. Download and transfer your Apple health data into the same directory as ```apple-health-parser.py``` and run this line of code:
  ```
  %run -i "apple-health-data-parser" "export.xml"
  ```
2. On the app.py file, you'll need to change ```strava_data``` and ```apple_data``` variables to the relative path of you're local csv files.

## Features
* Dropdown filters for day of week, distance and run type
* Performance charts
* Linear regression race performance indicator
* Shareable link

