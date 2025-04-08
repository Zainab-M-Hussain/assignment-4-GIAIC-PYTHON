def print_evens(start, end):
    """Print all even numbers between start and end (inclusive)."""
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number)

def main():
    try:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
        
        if start > end:
            print("Starting number should be less than or equal to ending number.")
            return
        
        print(f"Even numbers between {start} and {end}:")
        print_evens(start, end)
        
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main() 