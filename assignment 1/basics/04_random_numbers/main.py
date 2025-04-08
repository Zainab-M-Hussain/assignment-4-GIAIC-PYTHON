import random

def generate_random_numbers(start, end, count):
    numbers = []
    for _ in range(count):
        numbers.append(random.randint(start, end))
    return numbers

def main():
    print("Welcome to Random Numbers!")
    while True:
        try:
            print("\nEnter the range and count (or 'q' to quit):")
            print("Start of range:")
            start_input = input()
            
            if start_input.lower() == 'q':
                print("Goodbye!")
                break
                
            start = int(start_input)
            print("End of range:")
            end = int(input())
            print("How many numbers to generate:")
            count = int(input())
            
            if start > end:
                print("Start must be less than or equal to end!")
                continue
            if count <= 0:
                print("Count must be positive!")
                continue
                
            numbers = generate_random_numbers(start, end, count)
            print(f"\nRandom numbers: {numbers}")
            
        except ValueError:
            print("Please enter valid numbers!")

if __name__ == "__main__":
    main() 