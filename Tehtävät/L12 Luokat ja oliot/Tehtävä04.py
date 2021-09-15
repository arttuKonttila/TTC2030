import random
class Car:
    brand = ""
    model = ""
    price = 0,00
    def __init__(self, brand = "", model = "", price = 0):
        self.brand = brand
        self.model = model
        self.price = price
    def __str__(self):
        return self.brand + " " + self.model + " " + str(self.price)

car1 = Car("Audi", "", random.randint(1000, 10000))
car2 = Car("BMW", "", random.randint(1000, 10000))
car3 = Car("Ford", "", random.randint(1000, 10000))
car4 = Car("Opel", "", random.randint(1000, 10000))
car5 = Car("Skoda", "", random.randint(1000, 10000))
cars = [car1, car2, car3, car4, car5]

for car in cars:
    print(car.__str__())