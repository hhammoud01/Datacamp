#1- Add a descriptive title to the chart.
#2- Add a label for the y-axis.

# Lines
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

# Add a title
plt.title("TEST")

# Add y-axis label
plt.ylabel("TEST2")

# Legend
plt.legend()
# Display plot
plt.show()
