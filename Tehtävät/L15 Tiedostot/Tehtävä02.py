name_list = []
previous_names = []
filename = "nimet.txt"
#opens the file nimet.txt and saves all the names from the file into a list
try:
    with open(filename, "r") as fp:
        line = fp.readline()
        while line:
            name_list.append(line.strip())
            line = fp.readline()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Can't open the file, permission error!")

#prints the ammount of names that were saved
print("{} names found".format(len(name_list)))

#prints out how many times every name came up
for name in name_list:
    num = name_list.count(name)
    if previous_names.count(name) == 0:
        previous_names.append(name)
        print("{} came up {} times".format(name, num))