year_input = int(input("Insert a year: "))

def check_if_leapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "{0} is a leap year".format(year)
            else:
                return "{0} is not a a leap year".format(year)
        else:
            return "{0} is a leap year".format(year)
    else:
        return "{0} is not a leap year".format(year)

result = check_if_leapyear(year_input)
print(result)