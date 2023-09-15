# Day-73

# Popular Programming Language

This README provides an overview of the code for analyzing popular programming languages over time using Stack Exchange data. The code is written in Python and utilizes the Pandas and Matplotlib libraries for data manipulation and visualization.

## Get the Data

To obtain the data, you have two options:

1.  Use the provided .csv file.
2.  Run an SQL query on StackExchange to get fresh data. Follow the link to  [StackExchange](https://data.stackexchange.com/stackoverflow/query/675441/popular-programming-languages-per-over-time-eversql-com)  and run the provided SQL query to generate your own .csv file.

## Import Statements

The code begins by importing the necessary libraries, including Pandas and Matplotlib.

## Data Exploration

The data exploration section contains several challenges to understand the dataset:

-   Read the .csv file and store it in a Pandas dataframe.
-   Examine the first and last 5 rows of the dataframe.
-   Check the dimensions of the dataframe (number of rows and columns).
-   Count the number of entries in each column.
-   Calculate the total number of posts per language and identify the language with the highest total number of posts.
-   Determine the number of months of data available for each language and identify the language with the fewest months.

## Data Cleaning

In the data cleaning section, the date format is modified to make it more readable. The date column is converted from a string format (e.g., "2008-07-01 00:00:00") to a datetime object with the format "2008-07-01" using Pandas.

## Data Manipulation

This section includes challenges for data manipulation:

-   Create a new dataframe with modified date format.
-   Explore the dimensions of the new dataframe (rows and columns) and print the column names and first 5 rows.
-   Count the number of entries per programming language and identify potential reasons for different entry counts.

## Data Visualization with Matplotlib

Using Matplotlib, the code visualizes the data:

-   Plot a single programming language (e.g., Java) on a chart.
-   Plot two lines (e.g., for Java and Python) on the same chart.

## Smoothing out Time Series Data

To reduce noise in the time series data and identify trends, the code applies rolling mean. The rolling mean is calculated using the  `rolling()`  and  `mean()`  functions from the Pandas library.

For more details on the code implementation and usage, refer to the code comments and the respective documentation links provided