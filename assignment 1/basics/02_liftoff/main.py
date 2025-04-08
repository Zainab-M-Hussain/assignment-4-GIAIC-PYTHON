import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("LIFTOFF! 🚀")

def main():
    print("Welcome to Liftoff!")
    while True:
        try:
            print("\nEnter countdown time in seconds (or 'q' to quit):")
            user_input = input()
            
            if user_input.lower() == 'q':
                print("Goodbye!")
                break
                
            seconds = int(user_input)
            if seconds <= 0:
                print("Please enter a positive number!")
                continue
                
            countdown(seconds)
            
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main() 