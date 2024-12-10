# program for shoping cart

item = input("What an item would you like?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = quantity * price

print(f"You have bought {quantity}x {item}/s ")
print(f"Your total ${total} ")