#1- Create a bar plot of the time each officer spends on desk_work.
#2- Label that bar plot "Desk Work".
#3- Create a bar plot for field_work whose bottom is the height of desk_work.
#4- Label the field_work bars as "Field Work" and add a legend.

# Plot the number of hours spent on desk work
plt.bar(hours.officer, hours.desk_work, label='Desk Work')

# Plot the hours spent on field work on top of desk work
plt.bar(hours.officer, hours.field_work, bottom=hours.desk_work, label="Field Work")

# Add a legend
plt.legend("Field Work")

# Display the plot
plt.show()
