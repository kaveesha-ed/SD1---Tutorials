import random

num_rolls = 100
doubles = 0

for _ in range(num_rolls):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    if dice1 == dice2:
        doubles += 1

print(f'Out of {num_rolls} rolls, you rolled {doubles} doubles.')
