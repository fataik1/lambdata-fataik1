# my_lambdata/polos.py

#attributes / properties (NOUNS): size, style, color, texture, price
#methods (VERBS): wash, fold, pop collar


class Polo():
    def __init__(self, size, color):
        self.size = size
        self.color = color


    @property   
    def full_name(self):
        return f"{self.size} {self.color}"    


    def wash(self):
        print("WASHING THE {self.size}{self.color} POLO!")

    @staticmethod
    def fold(self):
        print("FOLDING THE POLO!")
        


if __name__ == "__main__":
#df = DataFrame(___________)
#df.coumns
#df.head()
    p1 = Polo(size="Small", color="Blue")
    print(p1.size, p1.color)
    p1.wash()

    p2 = Polo(size="Large", color="Yellow")
    print(p2.size, p2.color)
    p2.fold(self)