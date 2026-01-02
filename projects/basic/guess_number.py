# Number guessing game

import random

# function to generate a random number
def generate_number():
    return random.randint(1, 100)

# function to get user's guess
def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# function to check the guess
def check_guess(guess, number):
    if guess < number:
        return "Too low!"
    elif guess > number:
        return "Too high!"
    else:
        return "Correct!"   
    
def main():
    number_to_guess = generate_number()
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    
    while True:
        user_guess = get_user_guess()
        attempts += 1
        result = check_guess(user_guess, number_to_guess)
        print(result)
        
        if result == "Correct!":
            print(f"You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()