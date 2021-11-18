class Dog:

    #define color methods
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    #Define breed methods
    def setBreed(self, breed):
        self.breed = breed
    
    #return the breed

    def getBreed(self):
        return self.breed

#Object instances
Rodger = Dog()
Rodger.setColor("black")

Rodger.setBreed("Bulldog")
# Rodger = Dog.setBreed("Brown")

print("Rodger details:")
# print("Rodger is a ", Rodger.animal)
print("Rodger's color is ", Rodger.getColor())
print("Rodger's breed is ", Rodger.getBreed())
