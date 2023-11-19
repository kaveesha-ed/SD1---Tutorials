import random
hidden = random.randint(1,20)

while True :
    guess = int(input("Enter your guess number (number between 1 and 20)"))

    if guess < hidden:
        # If the guess is too low, inform the user and continue the loop
        print("Your guess is too low. Try a higher number.")
    elif guess > hidden:
        # If the guess is too high, inform the user and continue the loop
        print("Your guess is too high. Try a lower number.")
    else:
        print("WAS CORRECT")