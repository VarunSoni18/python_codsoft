import random

# Map choices to emojis
emoji_map = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
            (user == "scissors" and computer == "paper") or \
            (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def main():
    print("=== Welcome to Rock-Paper-Scissors Game 🎮 ===")
    user_score = 0
    computer_score = 0

    while True:
        # Get user input
        user_choice = input("Enter your choice (rock 🪨, paper 📄, scissors ✂️): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        # Get computer choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice} {emoji_map[computer_choice]}")
        print(f"You chose: {user_choice} {emoji_map[user_choice]}")

        # Determine winner
        winner = determine_winner(user_choice, computer_choice)
        if winner == "tie":
            print("It's a tie! 🤝")
        elif winner == "user":
            print("You win this round! 🎉")
            user_score += 1
        else:
            print("Computer wins this round! 💻")
            computer_score += 1

        # Display scores
        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

if __name__ == "__main__":
    main()
