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

car1 = Car("Skoda", "Octavia", 3000)
car2 = Car("Audi", "A4", 4000)
car3 = Car("Volvo", "V70", 5000)

print(car1.__str__())
print(car2.__str__())
print(car3.__str__())
print("Total price of the cars is: ", str(car1.price + car2.price + car3.price))