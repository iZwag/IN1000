# Oppg 4.1
# Make an empty list called called "steder"
elements = 5

steder = []

for i in range(0, elements):
    steder.append(input("Please enter a travel destination and hit ENTER: "))

# Oppg. 4.2
klesplagg = []
avreisedatoer = []

# NOTE: I am only making separate for-loops for the sake of the task.
# I'd consider putting them in the same otherwise.
for j in range(0, elements):
    klesplagg.append(input("Please enter a piece of clothing you're bringing: "))

for k in range(0, elements):
    avreisedatoer.append(input("Please enter a departure date: "))

# Oppg. 4.3
reiseplan = [steder, klesplagg, avreisedatoer]

# Oppg. 4.4
for l in range(0, elements):
    print("Destination: %s \tClothing: %s \tDeparture: %s" % (reiseplan[0][l], reiseplan[1][l], reiseplan[2][l]))

# Oppg. 4.5
# Prompts the user for input 1
i1 = int(input("Please enter which plan you want to view (integer 1-3): "))

# Checks if input 1 is within reasonable limits
if i1 <= len(reiseplan) and i1 > 0:
    
    # Prompts the user for input 2
    i2 = int(input("Please enter which item you want view (integer 1-%d): " % elements))
    # Checks if input 2 is within limits
    # If it is, the print that element
    if i2 <= len(reiseplan[i1-1]) and i2 > 0:
        print("You wanted to know: %s" % reiseplan[i1-1][i2-1])
    else:
        print("Ugyldig input!")
else:   
    print("Ugyldig input!")
