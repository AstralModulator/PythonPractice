import random as rnd

dice = {
    1: (
        "┌──────────┐\n"
        "│          │\n"
        "│     ●    │\n"
        "│          │\n"
        "└──────────┘"
    ),
    2: (
        "┌──────────┐\n"
        "│ ●        │\n"
        "│          │\n"
        "│        ● │\n"
        "└──────────┘"
    ),
    3: (
        "┌──────────┐\n"
        "│ ●        │\n"
        "│     ●    │\n"
        "│        ● │\n"
        "└──────────┘"
    ),
    4: (
        "┌──────────┐\n"
        "│ ●      ● │\n"
        "│          │\n"
        "│ ●      ● │\n"
        "└──────────┘"
    ),
    5: (
        "┌──────────┐\n"
        "│ ●      ● │\n"
        "│     ●    │\n"
        "│ ●      ● │\n"
        "└──────────┘"
    ),
    6: (
        "┌──────────┐\n"
        "│ ●      ● │\n"
        "│ ●      ● │\n"
        "│ ●      ● │\n"
        "└──────────┘"
    ),
}

dices = []
total = 0
num = int(input("Enter number of dice: "))
for die in range(num):
    dices.append(rnd.randint(1,6))
for die in dices:
    print(dice.get(die))
    total += die
print(f"Total: {total}")

