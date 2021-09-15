class Cat:
    def __init__(self, name="", color=""):
        self.name = name
        self.color = color
    
    def __str__(self):
        return self.name + ", " + "Color: " + self.color
    
    def miau(self):
        return self.name + " says: Meoooooow!"
    
    name = ""
    color = ""

kit = Cat("Kit", "black")
kat = Cat("Kat", "white")

print(kit.__str__())
print(kat.__str__())
print(kit.miau())
print(kat.miau())