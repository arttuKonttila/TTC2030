puppy = ["max", "snowball", "rex", "pug"]

try:
    puppy[4] = "geisha"
except IndexError:
    print("IndexError")
except:
    print("Something went wrong")