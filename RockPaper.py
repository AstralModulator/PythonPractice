import random as rnd

options = ('rock','paper', 'scissors')

print("Your options are: ")
for option in options:
    print(option,end = " ")
print()

continuee = True

while continuee:
    player = None
    computer = rnd.choice(options)
    while player not in options:
        player = input("Enter your choice: ")
    print(f"Computer chose: {computer}")
    if computer == player:
        print("It's a tie!")
    elif (computer == 'scissors' and player == 'rock') or (computer == 'paper' and player == 'scissors') or (computer == 'rock' and player == 'paper'):
        print("You win!")
    else:
        print("You lose!")
    if not input("Do you want to play again? (y/n): ").lower() == "y":
        continuee = False
print("Thank you for playing!")
