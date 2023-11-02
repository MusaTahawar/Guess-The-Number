import random

number = random.randint(10, 25)
attempts = 0
max_attempts = 9

print("Welcome to the Number Guessing Game!")
print(f"Guess a number between 10 and 25. You have {max_attempts} tries.")

while attempts < max_attempts:
    user_input = int(input("Enter your guess: "))

    if user_input < 10 or user_input > 25:
        print("Please guess a number between 10 and 25.")
        continue

    if user_input == number:
        attempts += 1
        print("Congratulations! You guessed it right!")
        print(f"You made it in {attempts} tries.")
        break
    elif user_input < number:
        print("A little higher.")
    else:
        print("A little lower.")

    attempts += 1
    print(f"You have {max_attempts - attempts} tries left.")

if attempts == max_attempts:
    print(f"Sorry, you've run out of tries. The number was {number}. Try again!")
