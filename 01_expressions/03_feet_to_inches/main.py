def main():
    while True:
        print("\nFeet/Inches Converter")
        print("1. Feet to Inches")
        print("2. Inches to Feet") 
        print("3. Quit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '3':
            break
            
        try:
            if choice == '1':
                feet = float(input("Enter number of feet: "))
                inches = feet * 12
                print(f"\n{feet} feet = {inches} inches")
                
            elif choice == '2':
                inches = float(input("Enter number of inches: "))
                feet = inches / 12
                print(f"\n{inches} inches = {feet:.2f} feet")
                
            else:
                print("\nInvalid choice. Please enter 1, 2, or 3.")
                
        except ValueError:
            print("\nPlease enter a valid number")
            continue

if __name__ == '__main__':
    main()
