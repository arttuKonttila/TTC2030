grade = []
user_input = "place_holder"

# Append grades to a list while input is not empty
while user_input != "":
    user_input = input("Enter registeration plate number: ")
    if user_input != "":
        grade.append(int(user_input))
    else:
        break

# print out the ammount of grades and the average of the grades
count = grade.__len__()

average = sum(grade)
average = average / count

print(str(count) + " grades were added, " + str(average) + " is the average for all of the grades.")