# Jeg tar gjerne tilbakemelding paa obligene paa norsk, men foretrekker aa programmere paa engelsk, hvis det er greit.

# Create list with three numbers
list_1 = [0, 11, 5]

# Add another number to the end of the list
list_1.append(17)

# Print the 1st and 3rd number
print("First element %d" % list_1[0])
print("Third element %d" % list_1[2])


# Create new, empty list
list_2 = []

# Loop 4 times and ask for name
for i in range(0,4):
    list_2.append(input("Please enter a first name, and press ENTER: "))

if "Jon" in list_2:
    print("Du husket meg!")
else:
    print("Glemte du meg?")


# Join the two lists into a third
str(list_1)
list_3 = list_1 + list_2

# Print list
print(list_3)

# Remove last 2 elements
list_3.pop()
list_3.pop()

# Print list again
print(list_3)

