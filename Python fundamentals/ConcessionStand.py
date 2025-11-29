#Concession Stand Program
menu = {
    "Khana" : 7.25,
    "Mo Mo" : 12.5,
    "Chowmein" : 5.45,
    "Popcorn" : 35.75,
    "IceCream" : 12.45
}

foods = []
total = 0

print("---------------------MENU---------------------------------------")
for key ,value in menu.items():
    print(f"{key}: {value}")

while True:
    food = input("Enter the food you would like to buy,Press 1 to quit: ")
    if food == "1":
        break
    elif menu.get(food) == None:
        print("The food is not on the MENU dumbass.")
    else:
        foods.append(food)
        total += menu.get(food)
print("--------------------YOUR CART-------------------------------")
for food in foods:
    print(food,end = "  ")
print()
print(f"Total cost: {total}")


