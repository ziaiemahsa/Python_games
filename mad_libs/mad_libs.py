# -*- coding: utf-8 -*-

'''Mad Libs'''

import re
import random

def load_stories(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        stories = content.split('---')
        stories = [story.strip() for story in stories if story.strip()]
        return stories
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []

def madlibs_game(story_template):
    """Run the Mad Libs game with a given story template."""
    placeholders = set(re.findall(r'\{(\w+)\}', story_template))

    inputs = {}
    for placeholder in placeholders:
        user_input = input(f"Enter a {placeholder}: ")
        inputs[placeholder] = user_input

    filled_story = story_template
    for placeholder, value in inputs.items():
        filled_story = filled_story.replace(f"{{{placeholder}}}", value)

    print("\nHere's your Mad Libs story:")
    print(filled_story)

def main():
    """Main function to run the Mad Libs game."""
    stories = load_stories('stories.txt')
    if not stories:
        return

    while True:
        story_template = random.choice(stories)
        madlibs_game(story_template)

        play_again = input("Would you like to play again (y/n)? ").lower()
        if play_again != 'y':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
