def menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Exit")

while True:
    menu()
    choice = input("Select an option: ")
    if choice in {'1', '2', '3', '4'}:
        if choice == '1':
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                print(f"Result: {num1 + num2}")
            except ValueError:
                print("Please enter valid numbers.")
        elif choice == '2':
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                print(f"Result: {num1 - num2}")
            except ValueError:
                print("Please enter valid numbers.")
        elif choice == '3':
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                print(f"Result: {num1 * num2}")
            except ValueError:
                print("Please enter valid numbers.")
        elif choice == '4':
            print("Exiting program.")
            break
    else:
        print("Invalid choice. Try again by entering 1, 2, 3, or 4.")
