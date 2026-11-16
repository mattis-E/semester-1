import random

# Get user to input how many random numbers they want

# Generate this many random numbers

# Write the random numbers to a file named random.txt, one number per line

num_input = int(input("How many random numbers do you want? "))
lst = []
with open("random_nums.txt", "w") as file:
    for i in range(num_input):
        file.write(str(random.randint(1, 100)) + "\n")