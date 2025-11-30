#Membership operator

secret_word = "APPLE"
is_playing = True
correct_guess = []
while is_playing:
    guess = input("Guess a letter: ")
    if guess in secret_word:
        correct_guess.append(guess)
        print("You guessed one correct letter.")
        if len(correct_guess) == len(secret_word):
            print("You have guessed all the correct letters.")
            print("The secret word is: {}".format(secret_word))
            is_playing=False
    else:
        print("Sorry, that's not in the secret word.")