"""
Password Generator - Day 05 Project
====================================
A simple password generator that creates random passwords based on user-specified
counts of letters, numbers, and symbols.

Features:
    - Customizable password length for each character type
    - Random selection from character pools
    - Shuffled output for better randomness

Usage:
    Run the script and follow the prompts to generate a password.
"""

import random as rand


# Character pools for password generation
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]

print("Welcome to the PyPassword Generator!")

# Get user preferences for password composition
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = []

# Generate random letters for the password
for l in range(0, nr_letters):
    password.append(rand.choice(letters))

# Generate random symbols for the password
for s in range(0, nr_symbols):
    password.append(rand.choice(symbols))

# Generate random numbers for the password
for n in range(0, nr_numbers):
    password.append(rand.choice(numbers))

# Display the password before shuffling (for comparison)
print("".join(password))

# Shuffle the password characters for better randomness
rand.shuffle(password)

# Display the final shuffled password
print("".join(password))
