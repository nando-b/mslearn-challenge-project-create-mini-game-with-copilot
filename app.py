import random

# create a terminal prompt for the user to input a word
# the user can choose one of the three options: rock, paper, or scissors and should be warned if they enter an invalid option
# the computer will randomly choose one of the three options
# the program will compare the user's input with the computer's input and determine who won
# the program will print the result of the game
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# the user can play again or exit the game
# the program will keep track of the number of games won by the user and the computer
# the program must handle user inputs, putting them in lowercase and ignoring any extra spaces
def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_wins = 0
    computer_wins = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_wins += 1
        elif result == "Computer wins!":
            computer_wins += 1

        print(f"User wins: {user_wins}")
        print(f"Computer wins: {computer_wins}")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

play_game()