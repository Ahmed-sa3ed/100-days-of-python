"""
Hangman Game - Day 07 Project
==============================
A classic word guessing game where the player tries to guess a word letter by letter.

Game Rules:
    - The computer selects a random word from a predefined list
    - Player has 6 attempts to guess the word
    - Each correct letter is revealed in its position
    - Each wrong guess reduces remaining lives by 1
    - Win by guessing all letters; lose when lives reach 0

Usage:
    Run the script and enter letters to guess the hidden word.
"""

import random as rand

# List of possible words to guess
words_list = ["ahmed", "mohamed", "mahmoud", "ali", "abbas", "zaflout"]

# Main game loop - allows multiple rounds
game_on = True

while game_on:
    # Select a random word for this round
    game_word = rand.choice(words_list)
    game_word_list = list(game_word)
    
    # Create a blanked representation of the word (e.g., "_______")
    word_blanked = "_" * len(game_word)
    word_blanked_list = list(word_blanked)
    
    print("This is your Word: " + word_blanked)
    
    # Round loop - continues until win or lose
    Level_on = True
    Points = 6  # Number of lives/attempts remaining
    
    while Level_on:
        # Get player's letter guess
        guiss = input("Enter Your Guiss: ").lower()
        
        # Check if the guessed letter is in the word
        if guiss in game_word_list:
            # Find the position of the letter
            i = game_word_list.index(guiss)
            # Reveal the letter in the blanked word
            word_blanked_list[i] = guiss
            # Mark the letter as used in the game word list
            game_word_list[i] = "_"
            print("GREAT now this is your word " + "".join(word_blanked_list))
        else:
            # Wrong guess - lose a life
            Points -= 1
            print(f"You only have {Points} lives!")
        
        # Check win condition - all letters revealed
        if "_" not in word_blanked_list:
            print("!!!! You have WON !!!!")
            Level_on = False
        
        # Check lose condition - no lives remaining
        if Points == 0:
            print("XXX YOU have LOST XXX")
            Level_on = False

    # Ask if player wants to play another round
    again = input("Do you want to play again? Y/N   ")
    if again.lower() == "n":
        game_on = False
