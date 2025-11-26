numbers = list(range(1, 51))
filtered_numbers = [n for n in numbers if n % 3 == 0 and n % 5 == 0]
if filtered_numbers:
    print("Numbers divisible by both 3 and 5:", filtered_numbers)
else:
    print("No numbers found divisible by both 3 and 5.")
