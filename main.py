from rock_paper_scissors import play_rps
from number_guess_game import play_number_guess

def main_menu():
    while True:
        print("""
=====================================
    🎮 MINI-GAMES ARCADE PORTAL 🎮
=====================================
    1- Play Rock Paper Scissors
    2- Play Number Guess Game
    3- Exit Arcade
=====================================
        """)
        
        choice = input("Select a game (1-3): ")
        
        if choice == "1":
            play_rps()  
        elif choice == "2":
            play_number_guess()  
        elif choice == "3":
            print("\nThank you for playing! See you next time! 👋")
            break
        else:
            print("Invalid selection! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main_menu()
