#1- Select rows of credit_records such that the column location is equal to 'Pet Paradise'.
#2- Which suspects purchased pet supplies before the kidnapping?

# Select purchases from 'Pet Paradise'
purchase = credit_records[credit_records.location == 'Pet Paradise']

# Display
print(purchase)

# QUESTION:
# which suspects purchased pet supplies before the kidnapping ?

# ANSWER:
# Fred Frequentist and Gertrude Cox
