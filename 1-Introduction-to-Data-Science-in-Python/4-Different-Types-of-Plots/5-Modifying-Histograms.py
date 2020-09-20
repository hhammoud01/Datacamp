#1- Create a histogram of the column weight from the DataFrame puppies.
#2- Change the number of bins to 50.
#3- Change the range to start at 5 and end at 35.

# Change the range to start at 5 and end at 35
plt.hist(puppies.weight,
        range=(5, 35))

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()
