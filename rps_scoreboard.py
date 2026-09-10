import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

for round_no in range(5):
    print("\nRound", round_no + 1)

    player = raw_input("Choose rock, paper or scissors: ").lower()
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if player not in choices:
        print("Invalid choice.")
        continue

    if player == computer:
        print("Draw!")

    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
        player_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

print("\nFinal Score")
print("You:", player_score)
print("Computer:", computer_score)
