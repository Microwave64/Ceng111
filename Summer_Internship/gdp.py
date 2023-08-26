import pandas as pd
import numpy as np
import statsmodels.api as sm
# Load the data
data = pd.read_csv("excel_table.csv") # Replace with the filename of your data
interest_rates = data["Interest rate"]
gdp = data["GDP"]
# Define the model
X = sm.add_constant(interest_rates) # Add a constant term to the independent variable
model = sm.OLS(gdp, X)
# Fit the model
results = model.fit()
# Print the summary of the regression results
print(results.summary())