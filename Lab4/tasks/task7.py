def fact(n):
    if n < 2:
        return 1
    return n * fact(n - 1)

def main():
    num = int(input("Enter number: "))
    return fact(num)

if __name__ == "__main__":
    print(main())