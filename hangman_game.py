import random

words = ["python", "computer", "programming", "developer", "keyboard"]
word = random.choice(words)

guessed = []
attempts = 6

while attempts > 0:
    display = ""

    for ch in word:
        if ch in guessed:
            display += ch
        else:
            display += "_"

    print("\nWord:", display)
    print("Attempts left:", attempts)

    if "_" not in display:
        print("You won!")
        break

    guess = raw_input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Enter one letter.")
        continue

    if guess in guessed:
        print("Already guessed.")
        continue

    guessed.append(guess)

    if guess not in word:
        attempts -= 1
        print("Wrong guess!")

if attempts == 0:
    print("\nYou lost!")
    print("The word was:", word)
