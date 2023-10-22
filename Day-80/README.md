
# Investigating the Causes of Puerperal Fever

## Background

This project analyzes monthly medical data from 1841 to 1849 to understand the causes of puerperal fever, a deadly infection contracted by women during childbirth in Vienna hospitals. The goal is to identify factors driving the high maternal mortality rate.

## Data 

The data covers monthly births, deaths, and mortality rates at two maternity clinics at the Vienna General Hospital. Additional analysis looks at mortality rates before and after June 1847 when handwashing protocols were introduced. 

## Analysis & Models

- Calculated mortality rates showing over 10% of delivering mothers died on average
- Visualized births and deaths over time, pointing to higher deaths in one clinic
- Compared clinic mortality rates, finding one had 3x more deaths 
- Split data before and after handwashing, finding a 90% drop in mortality
- Used statistical tests proving handwashing significantly lowered death rates

## Conclusions

The dramatic decline in mortality after handwashing indicates that puerperal fever was likely caused by poor hygiene. The analysis provides strong statistical evidence that handwashing protocols reduced childbed deaths, though the exact mechanism was not yet understood. This project shows the value of data and statistics in making data-driven medical discoveries.

## Key Libraries Used

- Pandas, NumPy for data manipulation
- Matplotlib, Plotly, Seaborn for visualization 
- SciPy for statistical testing
