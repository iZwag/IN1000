# Counts number of letters in a word
def count_letters(word):
    return len(word)

# Catalogues a sentence into a dictionary containing unique words and their frequency
def catalogue_sentence(string):
    
    # Splits the sentence into a list of words
    words = string.split()    
    
    # Make all wards lower case
    for w in range(len(words)):
        words[w] = words[w].lower()

    # Turns the list of words into a set of unique words
    unique_words = set(words)
    
    # Creates an empty dictionary called catalogue
    catalogue = dict()

    # Iterates through the unique words, setting the count to zero 
    for u_word in unique_words:
        
        count = 0
        
        # Increments the count when finding the unique word among the words in the sentence
        for word in range(len(words)):
            if u_word == words[word]:
                count += 1
        
        catalogue[u_word] = count
    
    return catalogue

# Prompts the user for a sentence. 
# Print is kept in Norwegian to comply with the task-format
sentence = input("Skriv en setning: ")

catalogue = catalogue_sentence(sentence)

# Prints number of words (not unique) in the sentence
print("Det er %d ord i setningen din." % len(sentence.split()))

# Prints unique words, with their correct frequency and word length 
for i in catalogue:
    print("Ordet \'%s\' \tforekommer %d gang(er), og har %d bokstav(er)." % (i, catalogue[i], count_letters(i)))

print(catalogue)
