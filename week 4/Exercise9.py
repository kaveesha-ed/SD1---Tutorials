while True:
    print("\nMenu:")
    print("1. Select option 1")
    print("2. Select option 2")
    print("3. Select option 3")
    print("4. Quit")

    try:
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            print("1 selected")
        elif choice == 2:
            print("2 selected")
        elif choice == 3:
            print("3 selected")
        elif choice == 4:
            print("Quit selected")
            break
        else:
            print("Option not recognized")
    except ValueError:
        print("Enter an integer choice (1-4)")
