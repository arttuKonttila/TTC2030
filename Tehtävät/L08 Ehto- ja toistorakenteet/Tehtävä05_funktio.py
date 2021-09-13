number = [0] * 5
number[0] = int(input("Anna ensimmäinen numero: "))
number[1] = int(input("Anna toinen numero: "))
number[2] = int(input("Anna kolmas numero: "))
number[3] = int(input("Anna neljäs numero: "))
number[4] = int(input("Anna viides numero: "))

def calculate_sum(number_array):
    sum = 0
    for n in number_array:
        if n > 0:
            sum = sum + n
    return sum

total = calculate_sum(number)
print("Sum is: ",total)