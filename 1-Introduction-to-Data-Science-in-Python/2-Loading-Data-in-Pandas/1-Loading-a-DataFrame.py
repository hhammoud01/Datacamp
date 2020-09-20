#1- Import the pandas module under the alias pd.
#2- Load the CSV "credit_records.csv" into a DataFrame called credit_records.
#3- Display the first five rows of credit_records using the .head() method.

# Import pandas under the alias pd
import pandas as pd

# Load the CSV "credit_records.csv"
credit_records = pd.read_csv("credit_records.csv")

# Display the first five rows of credit_records using the .head() method
print(credit_records.head())
