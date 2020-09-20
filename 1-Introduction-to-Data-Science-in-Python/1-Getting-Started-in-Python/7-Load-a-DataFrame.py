# 1- Use pd.read_csv to load data from a CSV file called ransom.csv. This file represents the frequency of each letter in the ransom note for Bayes.

# Import pandas
import pandas as pd

# Load the 'ransom.csv' into a DataFrame
r = pd.read_csv('ransom.csv')

# Display DataFrame
print(r)
