# -*- coding: utf-8 -*-

'''Rock Paper Scissors'''

import random

print("Rock, Paper, Scissors Rules:")
print("Rock crushes Scissors")
print("Scissors cuts Paper")
print("Paper covers Rock")

def get_choice(prompt, valid_choices):
    """Get a valid choice from the user or return a random choice for the PC."""
    choice = input(prompt).upper()
    while choice not in valid_choices:
        print(f"Invalid choice. Please choose from {', '.join(valid_choices)}.")
        choice = input(prompt).upper()
    return choice

def determine_winner(user_choice, pc_choice):
    """Determine the winner based on the choices."""
    if user_choice == pc_choice:
        return "Tie"
    elif (user_choice == 'R' and pc_choice == 'S') or \
         (user_choice == 'S' and pc_choice == 'P') or \
         (user_choice == 'P' and pc_choice == 'R'):
        return "User"
    else:
        return "PC"

def main():
    while True:
        try:
            max_score = int(input("Enter the maximum score to win: "))
            if max_score <= 0:
                raise ValueError("Score must be a positive integer.")
            break
        except ValueError as e:
            print(e)
            print("Please enter a valid positive integer.")

    user_score = 0
    pc_score = 0
    valid_choices = ['R', 'P', 'S']

    while user_score < max_score and pc_score < max_score:
        user_choice = get_choice("Enter your choice Rock(R), Paper(P), or Scissors(S): ", valid_choices)
        pc_choice = random.choice(valid_choices)
        print(f"PC chose: {pc_choice}")
        winner = determine_winner(user_choice, pc_choice)

        if winner == "Tie":
            print("It's a tie!")
        elif winner == "User":
            user_score += 1
            print("You win this round!")
        else:
            pc_score += 1
            print("PC wins this round!")
        print(f"Current Score - You: {user_score}, PC: {pc_score}")

    if user_score == max_score:
        print("Congratulations! You have won the game!")
    else:
        print("PC wins the game! Better luck next time.")

    play_again = input("Would you like to play again (y/n)? ").lower()
    if play_again == 'y':
        main()

if __name__ == "__main__":
    main()
