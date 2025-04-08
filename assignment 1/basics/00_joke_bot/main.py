import random

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a fake noodle? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call a fish with no eyes? Fsh!",
        "Why did the math book look sad? Because it had too many problems!"
    ]
    return random.choice(jokes)

def main():
    print("Welcome to the Joke Bot!")
    while True:
        print("\nWould you like to hear a joke? (yes/no)")
        response = input().lower()
        
        if response == 'yes':
            print("\n" + tell_joke())
        elif response == 'no':
            print("Okay, goodbye!")
            break
        else:
            print("Please answer with 'yes' or 'no'.")

if __name__ == "__main__":
    main() 