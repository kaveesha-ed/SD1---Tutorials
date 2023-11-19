choice = input("Enter '1' to convert from Celsius to Fahrenheit or '2' to convert from Fahrenheit to Celsius: ")

if choice == '1':
    c = float(input("Enter the temperature in Celsius: "))
    c = (c * 1.8) + 32
    print(f"{c}°C is equal to {c}°F")
elif choice == '2':
    f = float(input("Enter the temperature in Fahrenheit: "))
    converted_temp = (f - 32) / 1.8
    print(f"{f}°F is equal to {converted_temp}°C")
else:
    print("Invalid option entered.")
