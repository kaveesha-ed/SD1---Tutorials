# Function to show pizza toppings
def show_toppings(toppings):
    if not toppings:
        print("There are no toppings on your pizza.")
    else:
        print("The toppings on your pizza are:", end=" ")
        print(" ".join(toppings))

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
    print("c Change a topping")

    # Ask user what they want to do
    choice = input("What would you like to do? (add, remove, order, quit, startover, change): ").lower()

    if choice == 'a':
        topping = input("Type in a topping to add: ")
        toppingsList.append(topping)
        show_toppings(toppingsList)
    elif choice == 'r':
        topping_to_remove = input("What topping would you like to remove: ")
        if topping_to_remove in toppingsList:
            toppingsList.remove(topping_to_remove)
            show_toppings(toppingsList)
        else:
            print("That topping is not on your pizza.")
    elif choice == 'c':
        old_topping = input("What topping would you like to change: ")
        if old_topping in toppingsList:
            new_topping = input(f"What would you like to replace '{old_topping}' with: ")
            index = toppingsList.index(old_topping)
            toppingsList[index] = new_topping
            print("Topping changed successfully!")
            show_toppings(toppingsList)
        else:
            print("That topping is not on your pizza.")
    elif choice == 'o':
        if toppingsList:
            show_toppings(toppingsList)
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
        show_toppings(toppingsList)
