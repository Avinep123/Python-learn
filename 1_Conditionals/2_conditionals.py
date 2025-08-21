# age=int(input("Provide age : "))
# day="Wednesday"
# price=12 if age>=18 else 8

# if day=="Wednesday":
#     price=price-2

# print("Price for you is :", price)

from datetime import datetime

# Get current day name (e.g., 'Monday', 'Tuesday', etc.)
day = datetime.today().strftime('%A')

age = int(input("Provide age: "))

# Base price depending on age
price = 12 if age >= 18 else 8

# Discount if today is Wednesday
if day == "Wednesday":
    price -= 2

print("Today is", day)
print("Price for you is:", price)

