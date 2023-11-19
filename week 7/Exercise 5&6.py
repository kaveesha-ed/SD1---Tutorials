# Welcome message and instructions
print("Welcome to Cavendish Pizzeria - choose your toppings.")
print("When prompted, enter first letter or full word of operation.")

# List to hold the user’s topping choices
toppingsList = []

# Main loop
while True:
    print("\n---- Operations ----")
    print("a Add a topping")
    print("r Remove a topping")
    print("o Order the pizza")
    print("q Quit")
    print("s Start over")
    print("c Change a topping")  # Exercise 6 - New menu item for changing a topping

    # Ask user what they want to do
    choice = input("What would you like to do? (add, remove, order, quit, startover): ").lower()

    if choice == 'a':
        topping = input("Type in a topping to add: ")
        toppingsList.append(topping)
        if toppingsList:
            print("The toppings on your pizza are:")
            print(" ".join(toppingsList))
        else:
            print("Your pizza has no toppings yet.")
    elif choice == 'r':
        topping_to_remove = input("What topping would you like to remove: ")
        if topping_to_remove in toppingsList:
            toppingsList.remove(topping_to_remove)
            if toppingsList:
                print("The toppings on your pizza are:")
                print(" ".join(toppingsList))
            else:
                print("Your pizza has no toppings yet.")
        else:
            print("That topping is not on your pizza.")
    elif choice == 'c':  # New choice for changing a topping
        old_topping = input("What topping would you like to change: ")
        if old_topping in toppingsList:
            new_topping = input(f"What would you like to replace '{old_topping}' with: ")
            index = toppingsList.index(old_topping)
            toppingsList[index] = new_topping
            print("Topping changed successfully!")
            print("The toppings on your pizza are:")
            print(" ".join(toppingsList))
        else:
            print("That topping is not on your pizza.")
    elif choice == 'o':
        if toppingsList:
            print("The toppings on your pizza are:")
            print(" ".join(toppingsList))
            print("Thanks for your order!")
            toppingsList = []
        else:
            print("Your pizza has no toppings yet.")
    elif choice == 'q':
        break
    elif choice == 's':
        toppingsList = []
        print("Your pizza has been reset to start over.")
    else:
        print("I'm not sure what you said, please try again.")
        if toppingsList:
            print("The toppings on your pizza are:")
            print(" ".join(toppingsList))
        else:
            print("Your pizza has no toppings yet.")
