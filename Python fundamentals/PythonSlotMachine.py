#Slot machine program
import random as rnd

def gurren_laggan_spin_on():
    symbols = ["🍒","❤️","🔔"]
    spin_on = [rnd.choice(symbols) for _ in range(3)]
    return spin_on

def print_gurren_laggan(spin_on):
    print(*spin_on, sep="|")

def checkout(spin_on,bet):
    if spin_on.count("🍒") == 3:
        return bet*3
    elif spin_on.count("🔔") == 3:
        return bet*4
    elif spin_on.count("❤️") == 3:
        return bet*5
    else:
        return 0

def main():
    balance = 100
    print(f"Your balance is ${balance}")
    print("Welcome to the Python Slots Machine.")
    print("************************************")
    print("🍒|❤️|🔔")
    print("************************************")
    while balance > 0:
        bet = input("Enter your bet: ")
        while not bet.isdigit():
            print("Please enter a valid number.")
            bet = input("Enter your bet: ")
        bet = int(bet)
        balance -= bet
        spin_on = gurren_laggan_spin_on()
        print_gurren_laggan(spin_on)
        win = checkout(spin_on,bet)
        if win>0:
            print("You win!")
            balance += win
        else:
            print("You lose.")

        if not input("Would you like to continue? (y/n): ").lower() == "y":
            break
    print("Thank you for using Python Slots Machine.")
    print(f"Your balance is ${balance}")

if __name__ == "__main__":
    main()