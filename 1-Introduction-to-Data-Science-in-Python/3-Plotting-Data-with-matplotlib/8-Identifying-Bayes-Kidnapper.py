#1- Plot the letter frequencies from the ransom note. The x-values should be ransom.letter. The y-values should be ransom.frequency. The label should be the string 'Ransom'. The line should be dotted and gray.
#2- Plot a line for the data in suspect1. Use a keyword argument to label that line 'Fred Frequentist').
#3- Plot a line for the data in suspect2 (labeled 'Gertrude Cox').
#4- Label the x-axis (Letter) and the y-axis (Frequency), and add a legend.

# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label='Ransom', linestyle=':', color='gray')
plt.plot(suspect1.letter, suspect1.frequency, label='Fred Frequentist')
plt.plot(suspect2.letter, suspect2.frequency, label='Gertrude Cox')

# Add x- and y-labels
plt.xlabel("Letter")
plt.ylabel("Frequency")

# Add a legend
plt.legend("TEST")

# Display plot
plt.show()
