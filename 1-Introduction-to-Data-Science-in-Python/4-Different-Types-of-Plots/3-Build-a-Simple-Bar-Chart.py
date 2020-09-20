#1- Display the DataFrame hours using a print command.
#2- Create a bar chart of the column avg_hours_worked for each officer from the DataFrame hours.
#3- Use the column std_hours_worked (the standard deviation of the hours worked) to add error bars to the bar chart.

# Display the DataFrame hours using print
print(hours)

# Create a bar plot from the DataFrame hours
plt.bar(hours.officer, hours.avg_hours_worked,
        # Add error bars
        yerr=hours.std_hours_worked)

# Display the plot
plt.show()
