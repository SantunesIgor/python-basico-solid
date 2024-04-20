from car import Car

class Motorcycle(Car):

    def __init__(self, color, wheels, brand, fuel):
        Car.__init__(self, color, 2, brand, fuel)

    def abastecer(self, liters):
        if self.fuel + liters > 18:
            print('full fuel tank')
        else:
            self.fuel += liters
