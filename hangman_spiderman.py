# Angelu Yu's: Hangman Project (Spider-man Villains Edition)
# Random Module
import random

# Step 1 - Generating a random word
villain = ["rhino", "scorpion", "vulture", "chameleon", "kraven", "electro", "mysterio", "carnage", "venom", "kingpin", "shocker", "sandman", "lizard"]

#### Choose a Random Word (Variable)
chosen_villain = random.choice(villain)


# Step 2 - Displaying the blank lines for the chosen word
#Testing code
print(f'Pssst, the solution is {chosen_villain}.')

display = []
word_length = len(chosen_villain)
for _ in range(word_length):
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()

for position in range(word_length):
    letter = chosen_villain[position]
    if letter == guess:
        display[position] = letter

print(display)