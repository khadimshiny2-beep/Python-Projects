def Fahrenheit_to_Celsius(temp):
    return 5.0/9.0 * (temp - 32)

def Celsius_to_Farenheit(temp):
    return (temp * 1.8) + 32 

def main():
    try:
        print("=============== TEMPERATURE CONVERTER ===============")
        choice = int(input("1. Fahrenheit to Celsius\n2. Celsius to Farenheit\nChoice: "))
        match (choice):
            case 1:
                temp = float(input("Temperature: "))
                result = Fahrenheit_to_Celsius(temp)
                print(f"{temp}F = {result:.2f}C")
            case 2:
                temp = float(input("Temperature: "))
                result = Celsius_to_Farenheit(temp)
                print(f"{temp}C = {result:.2f}F")
            case _:
                print("Wrong input! Try again")
    except ValueError as e:
        print("Wrong input! Try again")
if __name__ == "__main__":
    main()