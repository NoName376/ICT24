REQUIRED_OPERATIONS = ("+", "-", "*", "/")


def main():

    try:
        inp1 = int(input("Enter 1 number: "))
        inp2 = int(input("Enter 2 number: "))
    except ValueError:
        return "Please enter valid numbers!"
        
    inp_oper = input("Enter operation: ")

    if inp_oper not in REQUIRED_OPERATIONS:
        return "operation is not support"
    if inp2 == 0 and inp_oper == "/":
        return "Division by zero"

    return eval(f"{inp1}{inp_oper}{inp2}")

if __name__ == "__main__":
    print(main())