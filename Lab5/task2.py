import random

target_number = random.randint(1, 100)
while True:
    guess = input("Guess the number (or enter 'q' to quit): ")
    if guess.lower() == 'q':
        print("Game exited. Target num is: " + str(target_number))
        break
    if guess.isdigit():
        guess = int(guess)
        if guess < target_number:
            print("Too low!")
        elif guess > target_number:
            print("Too high!")
        else:
            print("You guessed the number.")
            break
    else:
        print("Invalid input. Please enter a number between 1 and 100 or 'q' to quit.")
