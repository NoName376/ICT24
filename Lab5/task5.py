try:
    num = int(input("Enter a number: "))
    if num < 2:
        print("Not a prime number.")
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("Not a prime number.")
                break
        else:
            print("It's a prime number.")
except ValueError:
    print("Please enter a valid integer.")