
# Movie Budgets and Financial Performance Analysis

This project aims to analyze the relationship between movie budgets and financial performance using data scraped from  [the-numbers.com](https://www.the-numbers.com/movie/budgets). The dataset used for analysis was collected on May 1st, 2018.

## Table of Contents

1.  Introduction
2.  Import Statements
3.  Data Exploration and Cleaning
4.  Descriptive Statistics
5.  Investigating Zero Revenue Films
6.  Filtering on Multiple Conditions
7.  Unreleased Films
8.  Films that Lost Money
9.  Seaborn for Data Visualization: Bubble Charts
10.  Converting Years to Decades
11.  Separating "Old" and "New" Films
12.  Seaborn Regression Plots
13.  Running Linear Regression with scikit-learn
14.  Making Predictions with the Linear Model

## 1. Introduction

The project aims to explore the relationship between movie budgets and financial performance. The dataset used for analysis was scraped from  [the-numbers.com](https://www.the-numbers.com/movie/budgets)  on May 1st, 2018. The analysis will focus on answering questions related to average production budgets, worldwide gross revenue, profitability, and the impact of budgets on revenue.

## 2. Import Statements

The necessary libraries, including  `pandas`  and  `matplotlib.pyplot`, are imported for data analysis and visualization.

## 3. Data Exploration and Cleaning

The data is read from the CSV file  `cost_revenue_dirty.csv`. The dataset is explored to answer questions about its size, presence of NaN values, duplicate rows, and data types of columns. The data is further cleaned by converting the currency columns to numeric format and converting the  `Release_Date`  column to a Pandas Datetime type.

## 4. Descriptive Statistics

Descriptive statistics are calculated to gain insights into the dataset. The average production budget and worldwide gross revenue of films are computed. The minimum values for worldwide and domestic revenue are determined. The profitability of the bottom 25% of films is analyzed. The highest production budget and worldwide gross revenue of any film are identified, along with the revenue of the lowest and highest budget films.

## 5. Investigating Zero Revenue Films

The number of films with zero domestic and worldwide revenue is determined. The highest budget films that grossed nothing domestically and internationally are identified.

## 6. Filtering on Multiple Conditions

The data is filtered using the  `.query()`  function to create a subset of films that had some worldwide gross revenue but made zero revenue in the United States.

## 7. Unreleased Films

Films that were not released as of the data collection date (May 1st, 2018) are identified. The number of unreleased films included in the dataset is determined, and a new DataFrame called  `data_clean`  is created without these unreleased films.

## 8. Films that Lost Money

The percentage of films where the production costs exceeded the worldwide gross revenue is calculated.

## 9. Seaborn for Data Visualization: Bubble Charts

A bubble chart is created to visualize movie releases over time. The chart shows the relationship between the release date, budget, and worldwide gross revenue of films.

## 10. Converting Years to Decades

The release years of films are converted to decades. A new column called  `Decade`  is added to the  `data_clean`  DataFrame, indicating the decade of release.

## 11. Separating "Old" and "New" Films

The films are separated into two DataFrames:  `old_films`  and  `new_films`.  `old_films`  includes films released before 1970, while  `new_films`  includes films released from 1970 onwards. The number of films released prior to 1970 is determined, and the most expensive film made before 1970 is identified.

## 12. Seaborn Regression Plots

A Seaborn regression plot is created to visualize the relationship between budget and revenue for the  `new_films`  dataset. The plot includes a scatter plot and a linear regression line. The style of the chart is customized by setting the chart theme, axis limits, and color codes.

## 13. Running Linear Regression with scikit-learn

A linear regression model is fitted to the  `old_films`  dataset using scikit-learn. The intercept, slope, and r-squared value of the model are calculated to evaluate the model's performance.

## 14. Making Predictions with the Linear Model

The estimated global revenue for a film with a budget of $350 million is predicted using the linear regression model.

This readme file provides an overview of the analysis performed on the movie budgets and financial performance dataset. The code provided in the notebook can be executed to reproduce the results and explore the data further.