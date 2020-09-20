#1- From matplotlib, import the module pyplot under the alias plt
#2- Plot Officer Deshaun's hours worked using the columns day_of_week and hours_worked from deshaun.
#3- Display the plot

# From matplotlib, import pyplot under the alias plt
from matplotlib import pyplot as plt

# Plot Officer Deshaun's hours_worked vs. day_of_week
plt.plot(deshaun.day_of_week, deshaun.hours_worked)

# Display Deshaun's plot
plt.show()
