import datetime
seconds = int(input("Enter the ammount of seconds:"))
def time(seconds):
    date = str(datetime.timedelta(seconds=seconds))
    return date
print(time(seconds))