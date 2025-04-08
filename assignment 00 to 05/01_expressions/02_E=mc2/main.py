def main():
    SPEED_OF_LIGHT = 299792458  # meters per second

    while True:
        try:
            mass_str = input("Enter kilos of mass: ")
            if mass_str.lower() == 'quit':
                break
                
            mass = float(mass_str)
            
            print("\ne = m * C^2...")
            print(f"\nm = {mass} kg")
            print(f"\nC = {SPEED_OF_LIGHT} m/s")
            
            energy = mass * (SPEED_OF_LIGHT ** 2)
            print(f"\n{energy} joules of energy!")
            print()
            
        except ValueError:
            print("Please enter a valid number or 'quit' to exit")
            continue

if __name__ == '__main__':
    main()
