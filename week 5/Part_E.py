# Set up the secret word, number of turns, and empty guesses string
secret = "water"
turns = 6
guesses = ""

# Display introduction
print("Let's play Guess the Word")
print(f"You have {turns} turns to guess the word!")
print("_ " * len(secret))

# Loop until the player runs out of turns or guesses the word
while turns > 0:
    guess = input("Guess a letter: ").lower()  # Allow input in lowercase or uppercase
    guesses += guess  # Concatenate the guess to the guesses variable
    missed = 0  # Counter to track missed guesses

    # Iterate through each letter in the secret word
    for letter in secret:
        if letter in guesses:
            print(f'{letter} ', end='')  # Print the guessed letter
        else:
            print("_ ", end='')  # Print a dash for a letter not yet guessed
            missed += 1

    # Check if the word has been guessed
    if missed == 0:
        print("\nCongratulations! You've guessed the word!")
        break  # Terminate the loop if the word has been guessed

    # Reduce the number of turns if the guessed letter is not in the word
    if guess not in secret:
        turns -= 1
        print(f"\n'{guess}' is not in the word. You have {turns} turns left.")

# End of the game
if turns == 0:
    print("End of Game")
