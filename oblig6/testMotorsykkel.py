from motorsykkel import Motorsykkel

# Main-function to test the class created in the other file
def hovedprogram():
    # Creates three objects from the Motorsykkel-class
    bike1 = Motorsykkel("Suzuki", "ZZ2400", 0.0) 
    bike2 = Motorsykkel(reg_no="JZ9000", brand="Mitsubishi")
    bike3 = Motorsykkel(km=654.2)
    
    # Prints information for all them
    bike1.skrivUt()
    bike2.skrivUt()
    bike3.skrivUt()
    
    print("Last bike is driving 10 km...")
    
    # Adds 10km to the last bike
    bike3.kjor(10)
    
    print("New total km driven for last bike: %.1f" % bike3.hentKilometerstand())

# Runs the main-function
hovedprogram()
