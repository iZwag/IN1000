# Oppg. 2.1

# Initializes the input variable
inp = 1

# Creates an empty list for 2.2
numList = []

# While-loop that runs until the input is 0
while inp != 0:
    inp = int(input("Please enter an integer and hit ENTER (0 will end the loop): "))
    
    # This if-was added to protect list from getting a 0 added
    # A zero in the list is boring when checking for smallest number later    
    if inp != 0:
        # Adds the input to the end of the list
        numList.append(inp)

# Oppg. 2.3
# Uses a for-loop to print the contents of numList.
# This was done to solve the problem as described, print(numList) also works
for i in range(len(numList)):
    print(numList[i])

# Oppg. 2.4
# Initializes a sum, and then parses the list to add all the integers to a sum
minSum = 0

for j in range(len(numList)):
    minSum += numList[j]

print("The sum of all entered integers is: %d" % minSum)

# Oppg. 2.5
# Initializes min and max numbers with "real" values from the list
# The program shouldnt rely on assumptions on what values are in the list
smallest = numList[0]
biggest = numList[0]

# Finds the smallest number
for k in range(len(numList)):
    if numList[k] < smallest:
        smallest = numList[k]

# Finds the biggest number
for l in range(len(numList)):
    if numList[l] > biggest:
        biggest = numList[l]

print("The smallest number was %d, and the biggest number was %d." % (smallest, biggest))
