# Oppg. 1.1
# Function adding two integers and returning the sum
def adder(tall1, tall2):
    return tall1 + tall2

# Calling the function twice
print(adder(1, 2))
print(adder(2, 8))

# Function for oppg. 1.3
def tellForekomst(minTekst, minBokstav):
    
    # Initiates a counter to 0
    count = 0
    
    # Runs through the input text from start to end, one letter at a time
    for a in minTekst:
        # If the letter is a match, the counter is incremented
        if a == minBokstav:
            count += 1

    # Returns the result
    return count

# Oppg. 1.2 + 1.3
# Let the user write a text-string and a letter
text = input("Please enter a text and then hit ENTER: ")
letter = input("Now, please enter a single letter, and hit ENTER: ")

# The function is called in the format arguments, and a string is presented for the user 
print("The letter %s occurs %d times in the text %s" % (letter, tellForekomst(text, letter), text))    
