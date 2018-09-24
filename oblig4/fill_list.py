# Make a program that lets the user choose to generate a list of random
# number, or type in the numbers themselves.
# The user should also be able to choose the length of the list,
# and the range in which random numbers will generate.
# Must use lists and for-loops. Parts of this program can be useful
# at a later point when working with sorting.

import random 

random.seed()

print("Welcome to the program for filling lists of numbers!")

# Lets the user choose to generate numbers randomly or not
list_method = input("Do you want to generate numbers randomly (Y/n)? ")

# Take care of Yes-conditions, including Y, y, Yes, yes, and just ENTER
if (list_method.lower() == "y") or (list_method.lower() == "yes") or (list_method == ""):
    
    # Prompt user for the end-value of the range
    list_range = int(input("From 0 to what integer do you want numbers to be generated? "))
    
    # Handles possible invalid answer for list_range
    if list_range < 0:
    
        print("Negative numbers not allowed. Setting it to 100")
        list_range = 100

    elif list_range == 0:
      
        print("This makes for a non-existent range. Setting it to 100")
        list_range = 100
    
    # Unifies the answer for later        
    list_method = "y"

else:
    
    list_method = "n"

# Prompts the user for how many elements the list should contain
list_size = int(input("How many numbers should be in the list (integer above 0) "))

# Handles possible invalid answers for list_size
if list_size < 0:

    print("The list can't be of size negative.")

elif list_size == 0:

    print("Okay, no list at all then!")

else: 
    
    # Initiates the list of numbers
    number_list = []

    # Generates the list randomly
    if list_method == "y":
    
        print("Generating a random list of %d elements... " % list_size)    

        for i in range(0, list_size):
            number_list.append(random.randrange(list_range))

    # Generates the list by user-input
    elif list_method == "n":
    
        print("Please enter %d integer elements, will print result after: " % list_size)

        for i in range(0, list_size):
            number_list.append(int(input("Enter integer for list: ")))

    # Prints every element in a column
    for j in range(0, list_size):
        print(number_list[j])
    
