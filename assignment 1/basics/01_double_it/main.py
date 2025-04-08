def double_number(number):
    return number * 2

def main():
    print("Welcome to Double It!")
    while True:
        try:
            print("\nEnter a number to double (or 'q' to quit):")
            user_input = input()
            
            if user_input.lower() == 'q':
                print("Goodbye!")
                break
                
            number = float(user_input)
            result = double_number(number)
            print(f"The double of {number} is {result}")
            
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main() 