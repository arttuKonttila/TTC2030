import os
filename = "names.txt"
name_input = "*"
try:
    file = open(filename, "w")
    while name_input != "":
        name_input = input("Anna sukunimi, Tyhjä lopettaa: ")
        if name_input != "":
            file.write(name_input + "\n")
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Can't write the file, permission error!")
file.close()

try:
    fp = open(filename, "r")
    line = fp.readline()
    while line:
        print(line.strip())
        line = fp.readline()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Can't open the file, permission error!")
fp.close()


    



