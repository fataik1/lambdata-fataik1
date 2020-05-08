### Part 1 - Keeping it Classy
from random import randint


class Product():

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        #This is how we define our product
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def Stealability(self):
        #Chance of getting stolen
        steal = self.price / self.weight
        if steal < 0.5:
            return "Not so Stealable"

        elif steal < 1:
            return "Kind of Stealable"
    
        else:
            return "Very Stealable"
   
    def explode(self):
        """calculates the flammability times the weight"""
        explosion = self.flammability * self.weight
        if explosion < 10:
            return "...fizzle."
        if explosion  < 50:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """Classifies boxing gloves as a product"""
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "... it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight < 15:
            return "Hey that hurt!"
        else:
            return "Ouch"
