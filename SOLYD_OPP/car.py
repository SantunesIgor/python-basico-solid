class Car:
    def __init__(self, color, wheels, brand, fuel):
        self.color = color
        self.wheels = wheels
        self.brand = brand
        self.fuel = fuel

    def abastecer(self, liters):
        self.fuel += liters