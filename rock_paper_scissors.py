import random

# greet user
print("Hi! Let's play Rock, Paper, Scissors.")

# rules
print(
    "Rock beats scissors, scissors beats paper, paper beats rock. "
    "Same choice is a tie."
)

# game
choices = ["rock", "paper", "scissors"]
player = input("Your turn (rock, paper, or scissors): ")
computer = random.choice(choices)

print("Computer chose:", computer)

if player == computer:
    print("Tie!")
elif (
    (player == "rock" and computer == "scissors")
    or (player == "scissors" and computer == "paper")
    or (player == "paper" and computer == "rock")
):
    print("You win!")
else:
    print("Computer wins!")