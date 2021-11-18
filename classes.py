class Dog:
    #class variable
    animal = 'dog'
    #use _init_ constructor/Method
    def __init__(self, breed, color):
        
        #instantiate the variables
        self.breed = breed
        self.color = color

#use the variables
Rodger = Dog("Pug", "black")
Humpy = Dog("Bulldog", "Brown")

print("Rodger details:")
print("Rodger is a ", Rodger.animal)
print("Rodger's color is ", Rodger.color)
print("Rodger's breed is ", Rodger.breed)

#class viariable can be acccessed also
#using class name 
print("Class variable using class name")
print(Dog.animal)
