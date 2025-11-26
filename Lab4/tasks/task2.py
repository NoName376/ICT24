OPERATIONS = ("+", "-", "*", "/")

def main():
    while True:
        inp1 = input("Enter 1 number or 'q' to quit: ")

        if inp1 == "q":
            exit()

        try:
            num1 = int(inp1)
            num2 = int(input("Enter 2 number: "))
        except:
            print("Please enter valid numbers!")
     
        operation = input("Enter operation: ")

        if operation not in OPERATIONS:
            print("No such operation, try again")
            continue

        if num2 == 0 and operation == "/":
            print("Division by zero, try again")
            continue

        print(eval(f"{num1}{operation}{num2}"))

if __name__ == "__main__":
    main()