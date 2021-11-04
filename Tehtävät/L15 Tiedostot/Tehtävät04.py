import os
import decimal
filename_int = "integer_file.txt"
file_int = open(filename_int, "w")
filename_float = "float_file.txt"
file_float = open(filename_float, "w")
input_list = []
input_list.append(input("Enter an integer or a float number: "))
while input_list:
    for num in input_list:
        try: 
            if isinstance(int(num), int) == True:
                file_int.write(str(num) + ("\n"))
                input_list.append(input("Enter an integer or a float number: "))
            elif isinstance(float(num), float) == True:
                file_float.write(str(num) + "\n")
                input_list.append(input("Enter an integer or a float number: "))
            elif isinstance(num, decimal.Decimal) == True:
                file_float.write(str(num) + "\n")
                input_list.append(input("Enter an integer or a float number: "))
            else:
                break
        except ValueError:
            break