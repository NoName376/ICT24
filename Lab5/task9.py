try:
    number = int(input("Enter a number: "))
    if number > 0:
        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Please enter a valid integer.")
