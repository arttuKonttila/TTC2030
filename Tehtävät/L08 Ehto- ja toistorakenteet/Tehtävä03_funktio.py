user_input = int(input("Give an integer: "))

def check_int(user_input):
    if user_input == 10 or user_input == 20:
        return "Integer is 10 or 20"
    elif user_input == 100 or user_input == 200:
        return "Integer is 100 or 200"
    else:
        return str(user_input)

return_string = check_int(user_input)
print(return_string)