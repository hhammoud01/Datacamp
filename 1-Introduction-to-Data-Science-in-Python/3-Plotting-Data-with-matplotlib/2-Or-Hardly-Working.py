#1- Plot Officer Aditya's time worked with day_of_week on the x-axis and hours_worked on the y-axis.
#   Plot Officer Mengfei's time worked with day_of_week on the x-axis and hours_worked on the y-axis.
#2- Question
# One of the officers was removed from the investigation on Wednesday because of an emergency at a different station house. That office did not return on Thursday or Friday. Which color line represents that officer?

# Plot Officer Deshaun's hours_worked vs. day_of_week
plt.plot(deshaun.day_of_week, deshaun.hours_worked)

# Plot Officer Aditya's hours_worked vs. day_of_week
plt.plot(aditya.day_of_week, aditya.hours_worked)

# Plot Officer Mengfei's hours_worked vs. day_of_week
plt.plot(mengfei.day_of_week, mengfei.hours_worked)

# Display all three line plots
plt.show()

# QUESTION:
# One of the officers was removed from the investigation on Wednesday because of an emergency at a different station house. That office did not return on Thursday or Friday. Which color line represents that officer?

# ANSWER:
# orange
