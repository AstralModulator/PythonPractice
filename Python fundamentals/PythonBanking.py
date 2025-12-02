#Python Banking Program

def deposit():
    amount = float(input("How much do you want to deposit? \n $"))
    if amount <= 0:
        print("Sorry, But you have to enter a valid amount.")
        return 0
    else:
        print("...........Deposit Successfull..............")
        return amount

def withdraw(balance):
    amount = float(input("How much do you want to withdraw? \n $"))
    if amount > balance:
        print("Sorry, You don't have enough money.")
        return 0
    else:
        print("...........Withdraw Successfull............")
        return amount

def check_balance(balance):
    print("...........Checking Balance............")
    print(f"Your balance comes out to be: ${balance:,}")


def main():
    balance = 0
    is_running = True

    while is_running:
        print("________________________Python Banks___________________________")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")
        choice = input("Enter your choice: ")
        while choice not in ["1", "2", "3", "4"]:
            print("Please enter a valid choice.")
            choice = input("Enter your choice: ")
        match choice:
            case "1":
                balance += deposit()
            case "2":
                balance -= withdraw(balance)
            case "3":
                check_balance(balance)
            case "4":
                print("Thank you for using PythonBanking")
                is_running = False

if __name__ == "__main__":
    main()
