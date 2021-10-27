name_list = []
previous_names = []
sorted_name_list = []
filename = "nimet.txt"
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

print("{} names found".format(len(name_list)))

for name in name_list:
    num = name_list.count(name)
    if previous_names.count(name) == 0:
        previous_names.append(name)
        sorted_name_list.append("{} came up {} times".format(name, str(num)))

sorted_name_list.sort()
for name in sorted_name_list:
    print(name)