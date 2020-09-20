#1- Display the first five rows of the DataFrame and determine which columns to plot
#2- Create a scatter plot of the data in cellphone.

# Explore the data
print(cellphone.head())

# Create a scatter plot of the data from the DataFrame cellphone
plt.scatter(cellphone.x, cellphone.y)

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()
