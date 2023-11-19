hidden = 6

guess = int(input("Enter your guess number (number between 1 and 20)"))

while int((guess) != hidden):

    print(f"{guess} IS NOT CORRECT")
    guess = int(input("Enter your guess number (number between 1 and 20)"))

print(f"{guess} WAS CORRECT")