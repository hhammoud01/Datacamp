#1- Change the plotting style to "fivethirtyeight".
#2- Change the plotting style to "ggplot".
#3- View all styles by typing print(plt.style.available) in the console
#4- Pick one of those styles and see what it looks like

# Choose any of the styles
print(plt.style.available)
plt.style.use("seaborn-pastel")

# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()
