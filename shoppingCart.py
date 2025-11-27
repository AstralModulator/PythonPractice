#shopping cart problem

fruits = []
prices = []

while True:
    fruit = input("Enter the fruit you want.Press 1 to quit: ")
    if fruit == "1":
        break
    else:
        price = float(input("Enter the price of the fruit:$ "))
        fruits.append(fruit)
        prices.append(price)

print("-----------------------Your shopping Cart-----------------------")
for fruit in fruits:
    print(fruit,end="  ")
print()
total = 0
for price in prices:
    total += price
print(f"Your total is: ${total:.2f}")