import random

is_running = True

while is_running:
    # Generates a random number between 1 and 100 (representing the hidden sock)
    hidden_item = random.randint(1, 100)
    attempts = 10

    while True:
        if attempts > 0:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue
        else:
            print("You lost! Game over. The number was: {}".format(hidden_item))
            break

        difference = abs(guess - hidden_item)

        if guess != hidden_item:
            attempts -= 1

            if difference <= 3:
                print("VERY HOT 🔥")
            elif difference <= 10:
                print("HOT ☀️")
            elif difference <= 20:
                print("COLD ❄️")
            else:
                print("VERY COLD 🧊")

            print("Remaining attempts: {}".format(attempts))
        else:
            print("You won! The correct number was: {}".format(hidden_item))
            break

    play_again = input("Do you want to play again? (Y/N): ")
    if play_again.upper() == "Y":
        continue
    elif play_again.upper() == "N":
        print("See you next time!")
        is_running = False
