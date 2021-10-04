import decimal
def celToFah(aste):
    aste = decimal.Decimal(aste) * decimal.Decimal(1.8)
    aste = decimal.Decimal(aste) + decimal.Decimal(32.0)
    return "{:.01f}".format(aste)

def fahToCel(aste):
    aste = decimal.Decimal(aste) -  + decimal.Decimal(32.0)
    aste = decimal.Decimal(aste) *  + decimal.Decimal(0.5556)
    return "{:.01f}".format(aste)

input1 = decimal.Decimal(input("Enter fahrenheits:"))
input2 = decimal.Decimal(input("Enter celcius:"))

print(fahToCel(input1), "Celcius")
print(celToFah(input2), "Fahrenheit")

