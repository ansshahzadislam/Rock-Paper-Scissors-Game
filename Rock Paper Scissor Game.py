import random

# Function for taking user choice
def get_user_choice():
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

# Function for taking computer choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function for determining the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a TIE!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You WIN!"
    else:
        return "Computer WINS!"

# Main Function
def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Updating scores
        if result == "You WIN!":
            user_score += 1
        elif result == "Computer WINS!":
            computer_score += 1

        print(f"Your score: {user_score}, Computer's score: {computer_score}")

        play_again = input("Do you want to play again? (YES/NO): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    main()
