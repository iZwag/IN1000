# Creates a dictionary with given keys and values
dictionary = {"melk":14.90, "brod":24.90, "yoghurt":12.90, "pizza":39.90}

# Prints the dictionary
print(dictionary)

# Asks the user to input two items and their coherent prices
for i in range(0,2):
    item = input("Please enter an item and press ENTER: ")
    price = input("Please enter a price for %s and press ENTER: " % item)
    dictionary[item] = price

# Prints the resulting dictionary
print(dictionary)
