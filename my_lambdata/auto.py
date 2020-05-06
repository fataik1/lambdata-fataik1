class Auto():
    def __init__(self, make, model, year, color, num_wheels):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.num_wheels = num_wheels

    def drive(self):
        print("WE ARE DRIVING", self.model)

    def advertise(self):
        print("BUY OUR", self.model)

class Truck(Auto):
    def __init__(self, make, model, year, color, num_wheels, bed_size):
       super().__init__(make, model, year, color, num_wheels)
       self.bed_size = bed_size

if __name__ == "__main__":

    car = Auto("Toyota", "Prius", 2020, "Blue", 4)
    car.make
    car.model
    car.drive()
    car.advertise()

    car2 = Auto("Tesla", "Model S", 2020, "Blue", 4)
    car2.make
    car2.year
    car2.drive()
    car2.advertise()

    truck = Truck("Tesla", "Cybertruck", 2020, "Silver", 8, "4x6")
    truck.make
    truck.model
    truck.year
    truck.bed_size
    truck.drive()
    truck.advertise()