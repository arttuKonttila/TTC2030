import decimal


import decimal
def celToFah(aste):
    aste = aste * decimal.Decimal(1.8)
    aste = aste + decimal.Decimal(32.0)
    return "{:.01f}".format(aste)

def fahToCel(aste):
    aste = aste -  + decimal.Decimal(32.0)
    aste = aste *  + decimal.Decimal(0.5556)
    return "{:.01f}".format(aste)

input1 = decimal.Decimal(input("Enter fahrenheits:"))
input2 = decimal.Decimal(input("Enter celcius:"))

print(fahToCel(input1), "Celcius")
print(celToFah(input2), "Fahrenheit")

