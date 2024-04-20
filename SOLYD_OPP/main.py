from car import Car
from motorcycle import Motorcycle

gtrr35 = Car('white', 'vorsteiner', 'nissan', 74)
print("GT-R R35")
print('Color: ', gtrr35.color)
print('Wheels: ', gtrr35.wheels)
print('Brand: ', gtrr35.brand)
print('Fuel: ', gtrr35.fuel, '\n')

lambretta125 = Motorcycle('light blue', 'tubeless', 'lambretta', 9)
lambretta125.abastecer(90)
print('LAMBRETTA 125')
print('Color: ', lambretta125.color)
print('Wheels: ', lambretta125.wheels)
print('Brand: ', lambretta125.brand)
print('Fuel: ', lambretta125.fuel, '\n')
