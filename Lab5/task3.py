try:
    num_terms = int(input("Enter the number: "))
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        a, b = 1, 1
        for _ in range(num_terms):
            print(a)
            a, b = b, a + b
except ValueError:
    print("Please enter a valid positive integer.")
