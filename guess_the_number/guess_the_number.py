# -*- coding: utf-8 -*-

'''Guess the Number'''

import random

def user_guess_game(range_max):
    """Allow the user to guess a randomly generated number."""
    target_number = random.randint(1, range_max)
    user_guess = 0
    print(f"Try to guess the number I'm thinking of between 1 and {range_max}.")

    while user_guess != target_number:
        user_guess = int(input(f"Your guess (1-{range_max}): "))
        if user_guess < target_number:
            print("Too low! Try again.")
        elif user_guess > target_number:
            print("Too high! Try again.")

    print(f"Congratulations! You've guessed the number {target_number} correctly!")

def pc_guess_game(range_max):
    """Let the PC guess the number chosen by the user."""
    low = 1
    high = range_max
    feedback = ''
    print(f"Pick a number between 1 and {range_max} and let the PC guess it.")

    while feedback != 'c':
        if low <= high:
            pc_guess = random.randint(low, high)
        else:
            print("Error: The guessing range has become invalid.")
            return

        feedback = input(f"Is {pc_guess} too high (H), too low (L), or correct (C)? ").lower()

        if feedback == 'h':
            high = pc_guess - 1
        elif feedback == 'l':
            low = pc_guess + 1
        elif feedback != 'c':
            print("Invalid input. Please enter 'H', 'L', or 'C'.")

    print(f"The PC guessed your number {pc_guess} correctly!")

def main():
    range_max = 10

    while True:
        user_choice = input("Would you like to guess the number yourself (type 'me') or let the PC guess (type 'pc')? ").lower()

        if user_choice == 'me':
            user_guess_game(range_max)
        elif user_choice == 'pc':
            pc_guess_game(range_max)
        else:
            print("Invalid choice. Please type 'me' or 'pc'.")
            continue

        play_again = input("Would you like to play again (y/n)? ").lower()
        if play_again != 'y':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
