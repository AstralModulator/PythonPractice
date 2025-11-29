import random as rnd

low_limit = 0
high_limit = 100
answer = rnd.randint(low_limit,high_limit)

guesses = 0
is_running = True

print("Python Number Guessing Game")
print("You will be guessing the number between 0 and 100.")

while is_running:
    guess = input("Guess the number between 0 and 100: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < 0 and guess > 100:
            print("Your guess is out of range.")
        elif guess < answer:
            print("Your guess is too low.")
        elif guess > answer:
            print("Your guess is too high.")
        else:
            print(f"CORRECT! The number was {answer}")
            print(f"You guessed {guesses} times!")
            is_running = False

    else:
        print("Please enter a valid number.")

