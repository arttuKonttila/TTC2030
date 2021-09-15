class Human:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return "Nimi:" + self.name + " Ikä:" + str(self.age)

    name = ""
    age = 0

adam = Human("Adam", 18)
eva = Human("Eva", 18)
print(eva.__str__())
print(adam.__str__())