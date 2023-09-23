
# Google Trends and Financial Data Analysis

This repository contains code and instructions for analyzing the relationship between Google search trends and financial data. The goal is to explore whether the popularity of certain search terms corresponds to trends in stock prices or economic indicators.

## Data Sources

The analysis uses the following data sources:

-   [Unemployment Rate from FRED](https://fred.stlouisfed.org/series/UNRATE/): Provides the monthly unemployment rate.
-   [Google Trends](https://trends.google.com/trends/explore): Provides search volume data for specific keywords.
-   [Yahoo Finance](https://finance.yahoo.com/): Provides historical stock prices for Tesla and Bitcoin.

## Data Exploration

The first step is to explore the data and gain a better understanding of its structure. The code provided includes instructions and challenges to complete for each dataset, such as examining shapes, column names, and descriptive statistics.

## Data Cleaning

Before proceeding with the analysis, it's important to check for missing values in the datasets. The code provided helps you identify any missing values and remove them if necessary. Additionally, it guides you on converting string columns to datetime objects for better time series analysis.

## Data Visualization

Visualizations play a crucial role in analyzing the relationships between search trends and financial data. The repository includes code for creating visualizations to explore these relationships. It provides challenges to plot line charts, customize chart styles, adjust axis limits, add titles and labels, and explore different chart elements such as gridlines, linestyles, and markers.

## Completed Tasks

The analysis includes the following completed tasks:

1.  Data Exploration: Examined the shapes, column names, and descriptive statistics of the datasets.
2.  Data Cleaning: Checked for missing values in the datasets and removed them if necessary. Converted string columns to datetime objects.
3.  Data Visualization:
    -   Plotted line charts to analyze the relationship between Tesla stock price and search volume.
    -   Customized chart styles, including colors, line thickness, font sizes, and axis labels.
    -   Explored Bitcoin price and search volume using line charts with dashed lines and marker points.
    -   Plotted the search volume for "Unemployment Benefits" against the actual unemployment rate in the U.S.
    -   Calculated rolling averages for web searches and plotted them against the unemployment rate.

## Instructions

Feel free to explore the code and analysis provided in the repository. The README outlines the completed tasks, and the code contains comments and challenges for further exploration. You can also modify the code to conduct additional analyses or customize the visualizations according to your specific requirements.

Please note that the analysis assumes you have already downloaded the necessary CSV files and have them saved in the same folder as your notebook or script.