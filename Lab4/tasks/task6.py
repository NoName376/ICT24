def main():
    all_even = 0
    all_odd = 0
    for i in range(1, 101):
        if i % 2 == 0:
            all_even += i
        else:
            all_odd += i
    print(all_even, all_odd)

if __name__ == "__main__":
    main()