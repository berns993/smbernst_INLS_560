
garden = ['cucumber', 'tomato', 'greens', 'herbs']

for item in garden:
    if item == "greens":
        print(item.__add__(' (cruciferous vegetables)')) 
    else:
        print(item.capitalize())











'''
Original Sample:
cars = ['audi', 'bmw', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title)
'''