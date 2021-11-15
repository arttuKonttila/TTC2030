name_list = []
previous_names = []
sorted_name_list = []
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

#checks how many times names came up and saves them to a list for sorting
for name in name_list:
    num = name_list.count(name)
    if previous_names.count(name) == 0:
        previous_names.append(name)
        sorted_name_list.append("{} came up {} times".format(name, str(num)))

#sorts the list and prints it out
sorted_name_list.sort()
for name in sorted_name_list:
    print(name)
fp.close()
