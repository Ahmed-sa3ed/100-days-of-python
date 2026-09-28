# Password Generator - Day 05

A simple password generator that creates random passwords based on user-specified counts of letters, numbers, and symbols.

## Features

- Customizable password length for each character type (letters, numbers, symbols)
- Random selection from character pools
- Shuffled output for better randomness
- Simple command-line interface

## Requirements

- Python 3.x
- No external dependencies required

## Usage

```bash
python "Password Generator.py"
```

Follow the prompts to specify:
1. How many letters you want
2. How many symbols you want
3. How many numbers you want

The generator will display two passwords:
- One before shuffling (original order)
- One after shuffling (random order)

## How It Works

1. The program defines three character pools: letters (a-z), numbers (0-9), and symbols (!@#$%^&*()-+)
2. It asks the user for the desired count of each character type
3. It randomly selects characters from each pool
4. It shuffles all selected characters together
5. It displays the final shuffled password

## Example

```
Welcome to the PyPassword Generator!
How many letters would you like in your password?
4
How many symbols would you like?
2
How many numbers would you like?
2
abcdefghijklmnopqrstu0123456789!@#$%^&*()-+
4g!2k
```

## Code Structure

- Character arrays for letters, numbers, and symbols
- User input collection
- Random character selection using `random.choice()`
- Password shuffling using `random.shuffle()`
- Output display

## Learning Concepts

- Lists and list operations
- Random module usage
- User input handling
- String joining and manipulation
- Loops for iteration