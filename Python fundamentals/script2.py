from script1 import *

def favourite_film(film):
    return f"Your favourite film is {film}"

def main():
    film = input("Enter a film: ")
    print(favourite_film(film))
    print(favourite_food("Pop Corn"))

if __name__ == "__main__":
    main()