import os
import decimal
def isint(num):
    try:
        int(num)
        return True
    except:
        return False
def isfloat(num):
    try:
        float(num)
        return True
    except:
        return False
filename_int = "integer_file.txt"
file_int = open(filename_int, "w")
filename_float = "float_file.txt"
file_float = open(filename_float, "w")
input_list = []
input_list.append(input("Enter an integer or a float number: "))
for num in input_list:
    if(isint(num) == True or isfloat(num) == True):
        if(isint(num) == True):
                file_int.write(str(num) + "\n")
                input_list.append(input("Enter an integer or a float number: "))
        elif(isfloat(num) == True):
                file_float.write(str(num) + "\n")
                input_list.append(input("Enter an integer or a float number: "))
    else:
            print("Process stopped, input was not an integer or a float number")
file_float.close()
file_int.close()