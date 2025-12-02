#HangMan Game Python
import random as rnd
hangman_stages = {
    0: """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    1: """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    2: """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    3: """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    4: """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    5: """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    6: """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
}
def hint_print(hint):
    print(*hint, sep = " ")

def print_hangman(wrong_guesses):
    print("********************************")
    print(hangman_stages[wrong_guesses])
    print("*********************************")
def main():
    words = ["apple","coconut","banana","world","jesus","random","electricity","pineapple"]
    word = rnd.choice(words)
    is_playing = True
    guesses = set()
    wrong_guesses = 0
    hint = ["_"] * len(word)
    while is_playing:
        print_hangman(wrong_guesses)
        hint_print(hint)
        guess = input("Guess a letter: ")
        if not guess.isalpha() and len(guess) != 1:
            print("Enter a valid letter.")
            continue
        if guess in guesses:
            print("You already guessed that letter.")
            continue
        if guess in word:
            for index in range(len(word)):
                if guess == word[index]:
                    hint[index] = guess
        else:
            print("Sorry, that letter doesn't exist.")
            wrong_guesses += 1
        if "_" not in hint:
            print("Congratulations, you guessed the word!")

            is_playing = False
        if wrong_guesses == len(hangman_stages)-1:
            is_playing = False
            print(word)
            print_hangman(wrong_guesses)
            print("You are hanged")


if __name__ == "__main__":
    main()