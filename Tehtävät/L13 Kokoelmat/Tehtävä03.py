class Car:
    brand = ""
    registery_plate = ""
    def __init__(self, brand = "", registery_plate = ""):
        self.brand = brand
        self.registery_plate = registery_plate
    def __str__(self):
        return self.brand + " " + self.registery_plate

# create list of 10 cars
cars = []
cars.append(Car("skoda", "ABC-123"))
cars.append(Car("audi", "ERT-895"))
cars.append(Car("opel", "KSI-554"))
cars.append(Car("nissan", "LKI-001"))
cars.append(Car("chervolet", "CVW-619"))
cars.append(Car("lada", "ZXW-891"))
cars.append(Car("volvo", "BNM-340"))
cars.append(Car("mitsubishi", "PIO-237"))
cars.append(Car("hummer", "HOB-495"))
cars.append(Car("volkswagen", "LQR-767"))

# sort list by brand and print it out
cars.sort(key=lambda x: x.brand)
for car in cars:
    print(car.brand + " " + car.registery_plate)

# vertical line for demonstration purposes
print("---------------------")

#sort list by registery plate and print it out
cars.sort(key=lambda x: x.registery_plate)
for car in cars:
    print(car.brand + " " + car.registery_plate)

