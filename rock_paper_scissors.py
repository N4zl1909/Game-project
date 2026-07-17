import random

# Computer randomly chooses rock, paper, or scissors
computer = random.choice(["rock", "paper", "scissors"])

# Get user input and convert to lowercase for consistency
user = input("Enter rock, paper, or scissors: ").lower()

print("Computer's choice:", computer)

if user == computer:
    print("It's a tie!")
elif user == "rock" and computer == "paper":
    print("You lost!")
elif user == "scissors" and computer == "rock":
    print("You lost!")
elif user == "rock" and computer == "scissors":
    print("You won!")
elif user == "scissors" and computer == "paper":
    print("You won!")
elif user == "paper" and computer == "rock":
    print("You won!")
elif user == "paper" and computer == "scissors":
    print("You lost!")
else:
    print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")

print("Game over")
