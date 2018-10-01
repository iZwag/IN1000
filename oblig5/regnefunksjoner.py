# 1.1
# Function that takes two parameters and returns the sum 
def addisjon(number1, number2):
    return number1 + number2

# 1.2
# Function that subtracts the second number from the first one 
def subtraksjon(number1, number2):
    return number1 - number2

# 1.2
# Function that divides the first argument by the second
# Also added an assertion to test for 0 in denominator
def divisjon(number1, number2):
    assert(number2 != 0),"Division by 0 is illegal"
    return number1/number2

# 1.3
def tommerTilCm(antallTommer):
    assert(antallTommer > 0), "Inches must be greater than 0"
    return antallTommer * 2.54

# 1.4
def skrivBeregninger():
    
    print("Utregninger:")
    
    number1 = float(input("Skriv inn tall 1: "))
    number2 = float(input("Skriv inn tall 2: "))
    
    print("")
    print("Resultat av summering: %.1f" % addisjon(number1, number2))
    print("Resultat av subtraksjon: %.1f" % subtraksjon(number1, number2))
    print("Resultat av divisjon: %.1f" % divisjon(number1, number2))
    print("")
    print("Konvertering fra tommer til cm:")
    
    number3 = float(input("Skriv inn et tall: "))
    print("Resultat: %.2f" % tommerTilCm(number3))
    
    

# 1.1
# Prints the results of addition
print(addisjon(1,3))

# 1.2
# Testing all the other functions with assert
assert(subtraksjon(5,7) == -2),"Subtraction didn't work!"
assert(subtraksjon(1,-8) == 9),"Subtraction didn't work!"
assert(subtraksjon(-5,-5) == 0), "Subtraction didn't work!"

assert(divisjon(10,2) == 5),"Division didn't work!"
assert(divisjon(-2,2) == -1),"Division didn't work!"
assert(divisjon(-8,4) == -2),"Division didn't work!"

# 1.3
assert(tommerTilCm(3) > 0),"Converting from inches didn't work!"

# 1.4
skrivBeregninger()
