cost = float(input("Enter the cost of meal: "))
satisfaction = int(input("Enter satisfaction level [1 = Totally satisfied, 2 = Satisfied, 3 = Dissatisfied]: "))

if satisfaction == 1:
    tip_percentage = 0.20
    rate = "Totally satisfied"
elif satisfaction == 2:
    tip_percentage = 0.15
    rate = "Satisfied"
elif satisfaction == 3:
    tip_percentage = 0.10
    rate = "Dissatisfied"
else:
    print("Invalid satisfaction level entered.")
    exit()

tip_amount = cost * tip_percentage

print(f"You are {rate}.")
print(f"Tip: ${tip_amount:.2f}")
