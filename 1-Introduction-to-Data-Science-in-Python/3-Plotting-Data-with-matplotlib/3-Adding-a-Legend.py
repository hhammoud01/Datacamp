#1- Using the keyword label, label Deshaun's plot as "Deshaun".
#2- Add labels to Mengfei's ("Mengfei") and Aditya's ("Aditya") plots.
#3- Nothing is displaying yet! Add a command to make the legend display.
#4- Question
#   One of the officers did not start working on the case until Wednesday. Which officer?

# Officer Deshaun
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')

# Add a label to Aditya's plot
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')

# Add a label to Mengfei's plot
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

# Add a command to make the legend display
plt.legend()

# Display plot
plt.show()

# QUESTION:
# One of the officers did not start working on the case until Wednesday. Which officer?

# ANSWER:
# Mengfei
