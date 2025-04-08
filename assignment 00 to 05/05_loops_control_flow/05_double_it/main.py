def double_number(n):
    """Double the input number."""
    return n * 2

def main():
    try:
        number = float(input("Enter a number to double: "))
        result = double_number(number)
        print(f"The double of {number} is {result}")
        
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main() 