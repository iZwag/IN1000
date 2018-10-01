# 4.2
# Concatenates the two input strings 
def slaaSammen(string1, string2):
    return string1 + string2

# 4.3
# Prints out every element of the list on different lines    
def skrivUt(liste):
    for i in range(len(liste)):
        print(liste[i])

# 4.1
# Empty list 
mineOrd = []

# Initiates the command
command = "l"

# 4.4 
# The while-loop running until the user inputs "s"
while command != "s":

    command = input("Whatsup? Write i, u or s: ")

    if command == "i":
        text1 = input("Write a word or some text: ")
        text2 = input("Now, do the same again: ")
        mineOrd.append(slaaSammen(text1, text2))
    elif command == "u":
        skrivUt(mineOrd)
    elif command == "s":
        pass
    else:
        print("You must enter i, u or s!")

print("Bye, bye!") 
