import time

def countdown(n):
    """Perform a countdown from n to 1, then print 'Liftoff!'"""
    for i in range(n, 0, -1):
        print(i)
        time.sleep(1)
    print("Liftoff!")

def main():
    try:
        n = int(input("Enter the countdown number: "))
        if n <= 0:
            print("Please enter a positive number.")
            return
        
        print("Starting countdown...")
        countdown(n)
        
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main() 