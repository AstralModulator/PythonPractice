import random as rnd

options = ('rock','paper','scissors')
is_playing = True
print("You are playing rock paper scissors")
print(f"Your options are: {options}")

while is_playing:
    player = ""
    computer = rnd.choice(options)
    while player not in options:
        player = input("Enter your choice: ")
        if player not in options:
            print("Enter a valid option")
    print(f"Computer chose: {computer}")
    if (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print("you win Player")
    elif player == computer:
        print("It's a Draw")
    else:
        print("You Lose")
    if not input("Do you want to play again? (y/n): ").lower() == "y":
        is_playing = False

print("Thank you for playing")
