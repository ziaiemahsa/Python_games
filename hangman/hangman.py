# -*- coding: utf-8 -*-

'''Hangman'''

!pip install requests
import requests
import random

def get_random_word(url):
    """Fetch the list of words from the URL and return a random word."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if 'data' not in data or not isinstance(data['data'], list):
            raise ValueError("The expected 'data' field is missing or is not a list in the JSON response.")

        words = data['data']
        if not words:
            raise ValueError("The word list is empty.")
        return random.choice(words)

    except requests.RequestException as e:
        print(f"Error fetching the data: {e}")
    except ValueError as e:
        print(e)
    return None

def display_hangman(stage):
    """Print the Hangman drawing based on the current stage."""
    stages = [
        '''
         ------
         |    |
         |
         |
         |
         |
        ---
        ''',  # Empty (0 lives, full hangman will be drawn if the player loses)
        '''
         ------
         |    |
         |    O
         |
         |
         |
        ---
        ''',  # Head only (1 life left)
        '''
         ------
         |    |
         |    O
         |    |
         |
         |
        ---
        ''',  # Head and torso (2 lives left)
        '''
         ------
         |    |
         |    O
         |   /|
         |
         |
        ---
        ''',  # Head, torso, and one arm (3 lives left)
        '''
         ------
         |    |
         |    O
         |   /|\\
         |
         |
        ---
        ''',  # Head, torso, and two arms (4 lives left)
        '''
         ------
         |    |
         |    O
         |   /|\\
         |   /
         |
        ---
        ''',  # Head, torso, two arms, and one leg (5 lives left)
        '''
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        ---
        '''   # Full Hangman (6 lives left)
    ]
    print(stages[stage])

def hangman_game():
    """Run the Hangman game."""
    url = 'https://www.randomlists.com/data/words.json'
    word = get_random_word(url)

    if not word:
        print("Could not retrieve a word. Exiting the game.")
        return

    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    word_guessed = ['_'] * len(word)

    print("Welcome to Hangman!")

    while incorrect_guesses < max_incorrect_guesses and '_' in word_guessed:
        display_hangman(incorrect_guesses)
        print("Current word: " + ' '.join(word_guessed))
        guess = input("Guess a letter or enter '.' to give up: ").lower()

        if guess == '.':
            print(f"\nYou gave up! The word was: {word}")
            return

        if len(guess) != 1 or not guess.isalpha():
            print("\nPlease enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("\nYou've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    word_guessed[index] = guess
            print(f"\nGood guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"\nSorry, '{guess}' is not in the word.")

    display_hangman(incorrect_guesses)

    if '_' not in word_guessed:
        print("\nCongratulations! You've guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)

def main():
    while True:
        hangman_game()
        if input("Would you like to play again (y/n)? ").lower() != 'y':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
