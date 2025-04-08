import random

def get_wholesome_message():
    """Return a random wholesome message."""
    messages = [
        "You are doing great!",
        "Keep being awesome!",
        "You make the world a better place!",
        "Your smile is contagious!",
        "You are stronger than you think!",
        "Every day is a new opportunity!",
        "You are capable of amazing things!",
        "The world is better with you in it!",
        "You are making progress!",
        "Your potential is limitless!"
    ]
    return random.choice(messages)

def main():
    print("Welcome to the Wholesome Machine!")
    print("Press Enter to get a wholesome message (or 'q' to quit)")
    
    while True:
        user_input = input()
        if user_input.lower() == 'q':
            print("Goodbye! Stay wholesome!")
            break
        print(get_wholesome_message())
        print("\nPress Enter for another message (or 'q' to quit)")

if __name__ == "__main__":
    main() 