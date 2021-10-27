string_list = ["Arttu", "Kalle", "Jussi", "Jaakko", "Jere"]
result = False

while result != True:
    try:
        user_input_index = input("Enter index to save data on: ")
        user_input_data = input("Enter data to save on index location: ")
        string_list[int(user_input_index)] = str(user_input_data)
    except IndexError:
        print("Index was out of scope, try again")
        pass
    else:
        result = True

for string in string_list:
    print(string)
