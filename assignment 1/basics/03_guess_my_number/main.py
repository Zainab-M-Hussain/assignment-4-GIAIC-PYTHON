import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    
    print("\nI'm thinking of a number between 1 and 100.")
    
    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
                break
                
        except ValueError:
            print("Please enter a valid number!")

def main():
    print("Welcome to Guess My Number!")
    while True:
        print("\nWould you like to play? (yes/no)")
        response = input().lower()
        
        if response == 'yes':
            play_game()
        elif response == 'no':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Please answer with 'yes' or 'no'.")

if __name__ == "__main__":
    main() 