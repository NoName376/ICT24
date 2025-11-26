try:
    temp = float(input("Enter the temperature: "))
    conversion_type = input("Enter 'C' to convert from C to F or 'F' for F to C: ")

    if conversion_type.upper() == 'C':
        converted_temp = temp * 9/5 + 32
        print(f"{temp}°C is {converted_temp}°F")
    elif conversion_type.upper() == 'F':
        converted_temp = (temp - 32) * 5/9
        print(f"{temp}°F is {converted_temp}°C")
    else:
        print("Invalid option, please enter 'C' or 'F'.")
except ValueError:
    print("Please enter a valid numeric temperature.")
