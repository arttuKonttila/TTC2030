registery_plate = []
user_input = "place_holder"

# Append userinputs to a list while input is not empty
while user_input != "":
    user_input = input("Enter registeration plate number: ")
    if user_input != "":
        registery_plate.append(str(user_input))
    else:
        break

# sort list in alphabetical order
registery_plate.sort()
# print list out
for plate in registery_plate:
    print(plate)
