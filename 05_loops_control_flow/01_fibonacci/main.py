def fibonacci(n):
    """Generate the first n numbers in the Fibonacci sequence."""
    sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

def main():
    try:
        n = int(input("How many Fibonacci numbers would you like to generate? "))
        if n <= 0:
            print("Please enter a positive number.")
            return
        
        fib_sequence = fibonacci(n)
        print(f"The first {n} Fibonacci numbers are:")
        print(fib_sequence)
        
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main() 