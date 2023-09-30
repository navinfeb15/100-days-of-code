
# Android App Market Analysis

This repository contains the code and data for a comprehensive analysis of the Android app market by comparing thousands of apps in the Google Play store.

## About the Dataset

**Data Source:**
App and review data was scraped from the Google Play Store by Lavanya Gupta in 2018.

## Prerequisites

Before running the code in this notebook, make sure you have the following libraries installed:

- pandas
- plotly.express

You can install them using pip:

```shell
pip install pandas plotly
```

## Notebook Presentation

To ensure the notebook displays numeric output in decimal format, the following setting is applied:

```python
pd.options.display.float_format = '{:,.2f}'.format
```

## Usage

### 1. Read the Dataset

The dataset is read from the 'apps.csv' file using the following code:

```python
df_apps = pd.read_csv('apps.csv')
```

### 2. Data Cleaning

- Check the number of rows and columns in the dataset, column names, and view a sample of 5 rows.
- Drop the 'Last_Updated' and 'Android_Ver' columns.
- Find and remove rows with NaN values in the 'Ratings' column.
- Remove duplicates in the dataset.

### 3. Find Highest Rated Apps

Identify the highest rated apps in the dataset.

### 4. Find 5 Largest Apps in terms of Size (MBs)

Find the size in megabytes of the largest Android apps in the Google Play Store.

### 5. Find the 5 Apps with Most Reviews

Identify apps with the highest number of reviews.

### 6. Plotly Pie and Donut Charts

Visualize categorical data, specifically content ratings.

### 7. Numeric Type Conversion: Examine the Number of Installs

- Identify the number of apps with over 1 billion installations.
- Count the number of apps with only one installation.
- Convert the 'Installs' column to a numeric data type.

### 8. Find the Most Expensive Apps

Convert the price column to numeric data and investigate the top 20 most expensive apps.

### 9. Grouped Bar Charts

Analyze free vs. paid apps per category.

### 10. Box Plots

- Analyze lost downloads for paid apps.
- Examine revenue by app category.
- Explore paid app pricing strategies by category.

## Instructions

  

Feel free to explore the code and analysis provided in the repository. The README outlines the completed tasks, and the code contains comments and challenges for further exploration. You can also modify the code to conduct additional analyses or customize the visualizations according to your specific requirements.

  

Please note that the analysis assumes you have already downloaded the necessary CSV files and have them saved in the same folder as your notebook or script.