try:
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in meters): "))

    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            classification = "Underweight"
        elif 18.5 <= bmi < 25:
            classification = "Normal weight"
        elif 25 <= bmi < 30:
            classification = "Overweight"
        else:
            classification = "Obesity"
        print(f"Your BMI is {bmi:.2f} which is classified as {classification}.")
    else:
        print("Weight and height must be positive numbers.")
except ValueError:
    print("Please enter valid numeric values for weight and height.")
