import random
from hangman_words import word_list
from hangman_art import logo, stages

# Print Logo
print(logo)
print("Welcome to Hangman!")

# Choose a random word from the word_list
chosen_word = random.choice(word_list)

# Create a list of underscores to represent the letters in the chosen_word
display = ["_" for _ in chosen_word]

# Create a variable to keep track of the number of lives
lives = 6

# Create a list to keep track of guessed letters
guessed_letters = []

# Game loop
while True:
    # Print the current state of the game
    print(f"\n{' '.join(display)}")
    print(stages[lives])
    
    # Check if player has won
    if "_" not in display:
        print("Congratulations! You won!")
        break
    
    # Check if player has lost
    if lives == 0:
        print(f"You lost! The word was: {chosen_word}")
        break
    
    # Get player's guess
    guess = input("Guess a letter: ").lower()
    
    # Check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    
    # Check if the letter was already guessed
    if guess in guessed_letters:
        print(f"You've already guessed the letter {guess}")
        continue
    
    # Add the guess to guessed letters
    guessed_letters.append(guess)
    
    # Check if the guess is in the word
    if guess in chosen_word:
        # Update the display with the correct guess
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                display[i] = letter
    else:
        # Decrease lives if the guess is wrong
        lives -= 1
        print(f"The letter {guess} is not in the word.")
      
