import os

#path to desired directory
path = "C:/"
#fill list files with files names from path
files = os.listdir(path)
#print out all filenames from list files
for file in files:
    print(file)
#try to create ayho.txt in path
try:
    filename = "ayho.txt"
    fullname = os.path.join(path, filename)
    f = open(fullname, "w")
except:
    print("Error ocurred!")