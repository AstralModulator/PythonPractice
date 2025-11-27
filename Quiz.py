questions = (
    "How many planets in the Solar System?",
    "How many letters in the alphabet?",
    "Are you an idiot?"
)
options = (
    ("A.2","B.3","C.9","D.8"),
    ("A.26","B.24","C.25","D.18"),
    ("A.Yes","B.Definitely","C.Of Course","D.Yup")
)
answers = ('D','A','B')
guesses = []
question_num = 0
score = 0

for question in questions:
    print(question)
    print(options[question_num])
    guess = input("Enter your guess: ")
    if guess == answers[question_num]:
        score += 1
    guesses.append(guess)
    question_num += 1
print(f"Your guesses were: {guesses}")
print(f"Your total score was: {score}")