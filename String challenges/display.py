# Description: This program takes an item and its price as input and displays them in a formatted manner.
item = input("Enter the item: ")
price = input("Enter the price: ")

total_length = len(item) + len(price)

print(total_length)

dots = (25 - total_length) * "."

print(item + dots + price)
# Output: Enter the item: apple