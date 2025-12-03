#HangMan Game Python
import random as rnd
words = ["apple", "banana", "coconut", "sumit" ,"kumar", "das","suraj"]
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
    return print(*hint,sep = " ")
def hangman_print(wrong_guesses):
    print("******************************")
    print(hangman_stages[wrong_guesses])
    print("*******************************")
def main():
    word = rnd.choice(words)
    wrong_guesses = 0
    guesses = set()
    hint = ["_"] * len(word)
    is_playing = True
    print("Welcome to Hangman!")
    while is_playing:
        hangman_print(wrong_guesses)
        hint_print(hint)
        guess = input("Guess a letter: ")
        if guess != 0 and not guess.isalpha():
            print("Please enter a valid input.")
            continue
        if guess in guesses:
            print("You have already guessed that letter. Please try again.")
            continue
        guesses.add(guess)
        if guess not in word:
            wrong_guesses += 1
            print("Sorry, that's not in the word.")
        else:
            for i in range(len(word)):
                if word[i] == guess:
                    hint[i] = guess
        if "_" not in hint:
            print("You have successfully guessed the word.")
            is_playing = False
        if wrong_guesses >= 6:
            print("Sorry, you lose.")
            hangman_print(wrong_guesses)
            print("The word was", word)
            is_playing = False



    pass

if __name__ == '__main__':
    main()