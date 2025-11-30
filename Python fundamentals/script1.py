from script2 import *
def favourite_food(food):
    return f"Your favourite food is {food}"

def main():
    food = input("Enter you favourite food: ")
    print(favourite_food(food))
    film = input("Enter your favourite film: ")
    print(favourite_film(film))

if __name__ == "__main__":
    main()