# Food plan for three residents
matplan = { "Kari Nordmann": ["brod", "egg", "polser"], 
            "Magda Syversen": ["frokostblanding", "nudler", "burger"], 
            "Marco Polo": ["oatmeal", "bacon", "taco"]}

# Requests a name to check food plan for
person = input("Inquire the food plan for a resident, by typing their name: ")

# Prints feedback for the inquiry
if person in matplan:
    print(matplan[person])
else:
    print("Sorry, that person doesn't seem to be a resident here.")
