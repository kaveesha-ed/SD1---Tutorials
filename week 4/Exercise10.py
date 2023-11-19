import random

hidden_number = random.randint(1, 20)
max_attempts = 5
guesses = 0

print("Guess the number between 1 and 20!")

while guesses < max_attempts:
    guess = int(input("Enter your guess: "))
    guesses += 1

    if guess < hidden_number:
        print("Too low!")
    elif guess > hidden_number:
        print("Too high!")
    else:
        print(f"You got it in {guesses} guesses!")
        break
else:
    print(f"Not Guessed. The correct answer was {hidden_number}.")
