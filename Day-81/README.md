# Boston Housing Price Prediction

This Jupyter notebook builds a model to predict housing prices in 1970's Boston using the UCI Machine Learning housing dataset. 

## Contents

- Load and explore the Boston housing dataset
    - Check for missing values and duplicates
    - Visualize distributions of target and key features 
- Examine relationships between features using Seaborn pairplots and jointplots
- Split data into training and test sets
- Build linear regression model on training data 
- Evaluate model coefficients and residual errors  
- Improve model using log transformation on target variable
- Compare model performance on test data
- Use model to make price predictions on new data

The notebook follows the typical machine learning workflow:

1. Data exploration and cleaning
2. Visualization and feature analysis  
3. Train/test split
4. Model building 
5. Model evaluation and improvement
6. Making predictions

Key libraries used include Pandas, NumPy, Matplotlib, Seaborn, and Scikit-Learn.

The final model achieves a high accuracy in predicting housing prices based on features like number of rooms, pollution levels, and neighborhood demographics. This model could be deployed by a real estate company to estimate property values.