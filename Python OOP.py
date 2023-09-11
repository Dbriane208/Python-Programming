#1. PYTHON CLASS AND OBJECT
# We create a class using the keyword class then followed by the name of the class.
# A class can have objects and methods.

class Parrot:
    #class attributes
    name = ""
    age = 0

# Create an object
parrot = Parrot()
parrot.name = "Blu"
parrot.age = 10

# Access the attributes
print(f"{parrot.name} is {parrot.age} years old")

#2. PYTHON INHERITANCE
# Creating another class using the details of another classs without modifying them.

class Animal:

    def eat(self):
        return print("I can eat!")

    def sleep(self):
        print("I can sleep!")

#create instances
animal = Animal()
animal.eat()
animal.sleep()

#3. PYTHON ENCAPSULATION
# Refers to bundling of attributes and methods inside a single class.

class Computer:
    def __init__(self):
        self.__maxPrice = 900

    def sell(self):
        print("Selling Price : {}".format(self.__maxPrice))

    def setMaxPrice(self,price):
        self.__maxPrice = price

computer = Computer()
computer.sell()

#change the price. The price won't be changed because maxparice is a private variable
computer._maxPrice = 1000
computer.sell()
      
#using the setter function
computer.setMaxPrice(1000)
computer.sell()   

#4. POLYMORPHISM
# Refers to an entity tha can perform different operations in different scenarios

class polygon:

    #method to render a shape
    def render(self):
        print("Rendering a polygon!")

    def give(self):
        print("I am called by super!")    

class square(polygon):

    #method to render a square
    def render(self):
        print("Rnedering a square")

        #Call the method give using the super key word from the super class
        super().give()

#Creating an object of square
sq = square()
sq.render() 

         
