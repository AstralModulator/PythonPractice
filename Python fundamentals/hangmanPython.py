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
def print_hangman_stages(wrong_guesses):
    print("*****************************")
    print(hangman_stages[wrong_guesses])
    print("******************************")
    return
def main():
    word = rnd.choice(words)
    hint = ["_"] * len(word)
    wrong_guesses = 0
    guesses = set()
    print("You are playing Hangman By Python. Guess what you have?")
    is_playing = True
    while is_playing:
        print_hangman_stages(wrong_guesses)
        print(*hint, sep=" ")
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Sorry, that's not a letter.")
            continue
        if guess in guesses:
            print("You guessed the letter", guess)
            continue
        guesses.add(guess)
        if not guess in word:
            wrong_guesses += 1
            print("Sorry, that's not in the word.")
        else:
            print("You guessed a letter")
            for index in range(len(word)):
                if word[index] == guess:
                    hint[index] = word[index]
        if "_" not in hint:
            print("You Win!!!")
            is_playing = False
        if wrong_guesses >= 6:
            print("You have lost!")
            print(f"The word was: {word}")
            print_hangman_stages(wrong_guesses)
            is_playing = False





if __name__ == '__main__':
    main()