def main():
    print("This program converts between Fahrenheit and Celsius")
    question1 = input("Is the temperature in Fahrenheit or Celsius (f/c)? ").lower()
    
    if question1 == "f":
        question2 =float(input("Enter the temperature in fahrenheit :" ))
        celcius = (question2 - 32) * 5/9 
        print (celcius , "°C")
    elif question1 == "c":
        question2 = float(input("Enter the temperature in celsius: "))
        fahrenheit = (question2 * 9/5) + 32
        print(fahrenheit, "°F")
    else:
        print("Invalid input. Please enter 'f' or 'c'.")

if __name__ == "__main__":
    main()
