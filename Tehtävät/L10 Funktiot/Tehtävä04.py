import decimal
trip_length = int(input("Enter trip length in km:"))
price_liter = decimal.Decimal(input("Enter fuel price/liter:"))
fuel_consumpt = decimal.Decimal(input("Enter fuel consumption/100 km:"))

def calc_consumption(fuel_consumpt, price_liter, trip_length):
    total_consumption = decimal.Decimal(0.00)
    trip_length = trip_length / 100
    total_consumption = decimal.Decimal(trip_length) * fuel_consumpt

    total_fuel_price = total_consumption * price_liter
    print("Fuel:","{:.2f}".format(total_consumption) + " liter")
    print("Cost:","{:.2f}".format(total_fuel_price),"€")

calc_consumption(fuel_consumpt, price_liter, trip_length)