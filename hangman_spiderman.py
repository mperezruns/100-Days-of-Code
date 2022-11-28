# Angelu Yu's: Hangman Project (Spider-man Villains Edition)
# Random Module
import random

# Step 1 - Generating a random word
villain = ["rhino", "scorpion", "vulture", "chameleon", "kraven", "electro", "mysterio", "carnage", "venom", "kingpin", "shocker", "sandman", "lizard"]

#### Choose a Random Word (Variable)
chosen_villain = random.choice(villain)

# Testing
#print(chosen_villain)

# Asking a user to guess a letter and assign their answer to a vairable
guess = input("Guess a letter:").lower()

# Check if the letter the user guessed (guess)
for letter in chosen_villain:
    if letter == guess:
        print("Correct")
    else:
        print("Wrong")