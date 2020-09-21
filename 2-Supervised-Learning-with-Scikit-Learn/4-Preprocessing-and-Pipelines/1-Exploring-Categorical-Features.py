"""
Import pandas as pd.
Read the CSV file 'gapminder.csv' into a DataFrame called df.
Use pandas to create a boxplot showing the variation of life expectancy ('life') by region ('Region'). To do so, pass the column names in to df.boxplot() (in that order).
"""

# Import pandas
import pandas as pd

# Read 'gapminder.csv' into a DataFrame: df
df = pd.read_csv('gapminder.csv')

# Create a boxplot of life expectancy per region
df.boxplot(column='life', by='Region', rot=60)

# Show the plot
plt.show()
