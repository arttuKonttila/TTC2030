# import decimal variable type from the library
from decimal import Decimal as d

# declare balance ammount
balance = d(2000)
# print balance ammount on the console
print("Bank account balance: ", balance, "€")
# ask the user for the ammount of euros and cents to be added on the balance
user_input_euros = d(input("How many euros will be added to the balance?: "))
user_input_cents = d(input("How many cents will be added to the balance?: "))
# convert user_input_cents from euros to cents
user_input_cents = user_input_cents / 100
# calculate the total of both numbers
total_added_ammount = user_input_euros + user_input_cents
# add the ammount into the total balance ammount
balance = balance + total_added_ammount
# print out the total balance ammount
print("Bank account balance: ", balance, "€")