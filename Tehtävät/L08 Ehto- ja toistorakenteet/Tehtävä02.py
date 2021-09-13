user_input_first = int(input("Input first integer: "))
user_input_second = int(input("Input second integer: "))
user_input_third = int(input("Input third integer: "))

if user_input_first > user_input_second and user_input_first > user_input_third:
    print("Max value: ", user_input_first)
elif user_input_second > user_input_third and user_input_second > user_input_first:
    print("Max value: ", user_input_second)
elif user_input_third > user_input_first and user_input_third > user_input_second:
    print("Max value: ", user_input_third)