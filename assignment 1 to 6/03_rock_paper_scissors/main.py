import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return "user"
    return "computer"

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    
    user_score = 0
    computer_score = 0
    
    while True:
        print(f"\nScore - You: {user_score}, Computer: {computer_score}")
        
        # Get choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        # Show choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine and display winner
        result = determine_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        
        # Ask to play again
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if not play_again.startswith('y'):
            print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
            break

if __name__ == "__main__":
    rock_paper_scissors() 