# Class for motorcycle
class Motorsykkel:
    # Constructor method 
    def __init__(self, brand="Toyota", reg_no="OK1337", km=0.0):
        self.brand = brand
        self.reg_no = reg_no
        self.km = km
    
    # A function to drive a specified number of kms, adding to the total km
    def kjor(self, km):
        self.km += km

    # Prints the total km
    def hentKilometerstand(self):
        return self.km

    # Prints the three different data points for the motorcycle
    def skrivUt(self):
        print("KJORETOYDATA")
        print("Merke: %s" % self.brand)
        print("Registreringsnummer: %s" % self.reg_no)
        print("Kilometerstand: %.1f" % self.km)

