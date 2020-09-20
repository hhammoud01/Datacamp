#1- Create a variable called plate that represents the observed license plate: the first three letters were FRQ, but the witness couldn't see the final 4 letters. Use asterisks (*) to represent missing letters.

#2- Call lookup_plate() using the variable plate.

#3- Calling lookup_plate() with the license plate FRQ**** produced too many results. Luckily, lookup_plate() also accepts a keyword argument: color. Use the color of the car ('Green') to get a smaller list.

# Define plate to represent a plate beginning with FRQ
# Use * to represent the missing four letters
plate = 'FRQ****'

# Call the function lookup_plate()
lookup_plate(plate)

# Call lookup_plate() with the keyword argument for color
lookup_plate(plate, color='Green')
