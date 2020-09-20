#1- Inspect the DataFrame mpr using info().
#2- Correct the mistakes in the code so that it runs without errors.
#3- Why did this code generate an error? name = mpr.Dog Name

# Use info() to inspect mpr
print(mpr.info())

# The following code contains one or more errors
# Correct the mistakes in the code so that it runs without errors

# Select column "Dog Name" from mpr
name = mpr["Dog Name"]

# Select column "Missing?" from mpr
is_missing = mpr["Missing?"]

# Display the columns
print(name)
print(is_missing)

# Why did this code generate an error?
#   name = mpr.Dog Name

# ANSWER: IF A COLUMN NAME CONTAINS A SPACE, THEN IT NEEDS TO BE IN
#           BRACKETS AND STRING NOTATION.
