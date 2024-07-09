# Running Dashboard

## Purpose of the project
This web application creates a dashboard of running statistics and trends from exported Strava and Apple Health data. By pairng these two datasets together, this app intends to help runners view their performance statistics and progress overtime. The race pace predictor is also a useful tool for runners to view their estimated performance on race days based off their current traninng efforts, and can therefore make adjustments to their training plan.

Try out the app here: https://running-dashboard.onrender.com/

![Untitled design (3)](https://github.com/Raine0554/running-dashboard/assets/96808637/9366c3af-9605-4380-b978-21909c6f699e)

<img width="1454" alt="Screenshot 2024-07-09 at 8 51 37 pm" src="https://github.com/Raine0554/running-dashboard/assets/96808637/401b6a20-129c-47c7-8128-d90b4642bd45">


## Why I made this application
As a beginner runner, 
Strava is good at analysing each run, but is not good at comparing runs or showing progress overtime (e.g how much your pace has improved; overall average, pace per distance types)
I want to see how much I’ve improved overtime. I also want to see what my predicted race performance will be in October based on my current progression trends (apply linear regression model).

Additionally, I want to combine my health data, analyse energy expenditure trends throughout the week so that I can gauge my calorie intake so I can maintain a calorie deficit without feeling hungry. 

## How to use this application
The link to the dashboard sources its data from my own local csv files that I exported from the Strava and Apple Health apps. Here's what you can do if you'd like to use this dashboard for your own data:


### Requirements 


### How to export Strava and Apple Health Data
Change the data paths in app.py to you're own csv files. 

## Improvements 
I update this application on an ongoing basis, improving or adding new features as I become a more experienced runner and programmer. Here's a list of things that I'm currently working on for this project:

* Using Apple gps data to plot heatmap
* Summary row connected to drop down filters
* Make functions for data loading and cleaning more robust
* Not specific to just data
* Implement linear regression model/time series forecasting
* Even just on jupyter notebook for now

