user_input = input("Anna luku: ")
user_input_sum = int(user_input)
luku_counter = 1
while user_input != "":
    user_input = input("Anna luku: ")
    if user_input == "":
        break
    user_input_sum += int(user_input)
    luku_counter += 1

        
print("Lukuja annettu: ", luku_counter)
print("Lukujen summa: ", user_input_sum)