total = 0  # sum of scores
count = 0  # number of scores entered

# get one score & convert string to integer
score = int(input("Enter score, (Enter -9 to end): "))

# Check if the first input is -9
if score == -9:
    print("No scores entered.")
else:
    while score != -9:
        total += score
        count += 1
        score = int(input("Enter score, (Enter -9 to end): "))

    # Check if at least one score has been entered before calculating average
    if count > 0:
        average = float(total) / count
        print("Class average is", average)
    else:
        print("No scores entered.")
