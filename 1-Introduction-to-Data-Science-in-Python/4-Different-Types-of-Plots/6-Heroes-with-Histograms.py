#1- Create a histogram of gravel.radius.
#2- Modify the histogram such that the histogram is divided into 40 bins and the range is from 2 to 8.
#3- Normalize your histogram so that the sum of the bins adds to 1.
#4- Label the x-axis (Gravel Radius (mm)), the y-axis (Frequency), and the title(Sample from Shoeprint).

# Create a histogram
plt.hist(gravel.radius,
         bins=40,
         range=(2, 8),
         density=True)

# Label plot
plt.xlabel('Gravel Radius (mm)')
plt.ylabel('Frequency')
plt.title('Sample from Shoeprint')

# Display histogram
plt.show()
