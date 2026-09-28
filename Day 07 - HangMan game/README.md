# HangMan Game - Day 07

A classic word guessing game where the player tries to guess a hidden word letter by letter.

## Features

- Word selection from a predefined list
- 6 attempts (lives) per round
- Letter-by-letter guessing
- Visual feedback of revealed letters
- Multiple round support
- Win/loss detection

## Requirements

- Python 3.x
- No external dependencies required

## Usage

```bash
python "HangMan game.py"
```

Enter letters to guess the hidden word. You have 6 lives - each wrong guess costs one life.

## Game Rules

1. The computer selects a random word from the word list
2. The word is displayed as underscores (e.g., "_______")
3. You guess one letter at a time
4. Correct letters are revealed in their positions
5. Wrong guesses reduce your remaining lives
6. Win by revealing all letters before running out of lives
7. You can play multiple rounds

## Example

```
This is your Word: _______
Enter Your Guiss: a
GREAT now this is your word a______
Enter Your Guiss: z
You only have 5 lives!
...
!!!! You have WON !!!!
Do you want to play again? Y/N
```

## Code Structure

- `words_list`: Array of possible words to guess
- `game_word`: The randomly selected word for the current round
- `word_blanked_list`: Display representation with underscores
- `Points`: Remaining lives (starts at 6)
- Main game loop with nested round loop

## Learning Concepts

- While loops for game flow
- List manipulation
- String operations
- Conditional logic
- User input handling