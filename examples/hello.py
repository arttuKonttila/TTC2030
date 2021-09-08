#import datetime library
from datetime import datetime

now = datetime.now()
current_date = now.strftime("%d/%m/%y")

print("Arttu Konttila")
print(current_date)
print("Hello World!")