# Creates a class for a dog
class Hund:
    # Constructor method. Setting metthet to default 10 is a part of the task
    def __init__(self, alder=0, vekt=0.0, metthet=10):
        self.alder = alder
        self.vekt = vekt
        self.metthet = metthet

    # Getter for age
    def get_alder(self):
        return self.alder

    # Getter for weight
    def get_vekt(self):
        return self.vekt
    
    # Prints weight - not required, but good for conveniance
    def print_vekt(self):
        print("Hunden veier %.1f" % self.vekt)

    # Makes the dog run, with reduction in fullness and weight
    def spring(self):
        print("Hunden springer!")
        
        self.metthet -= 1
        
        if self.metthet < 5:
            self.vekt -= 1
        
    # Makes the dog eat a specified amount, increasing fullness and possibly weight
    def spis(self, mengde):
        print("Hunden spiser %d" % mengde)
        
        self.metthet += mengde
    
        if self.metthet > 7:
            self.vekt += 1

