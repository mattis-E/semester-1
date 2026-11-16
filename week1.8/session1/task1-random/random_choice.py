import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

# Display the chosen names, one per line

num_inps = int(input("How many names do you want? "))

buffer = []
with open("names.txt", "r") as file:
    buffer = file.readlines()

chosen = random.sample(buffer, num_inps)
print(chosen)