# Week 1.2, Session 1: Task 3

fruit = ("apple", "banana", "cherry")
print(fruit)

# Find and display position of "banana"
print(f"Index of 'banana': {fruit.index("banana")}")

# Display how many times "cherry" occurs
print(f"Occurrences of 'cherry': {fruit.count("cherry")}")

# Display how many times "strawberry" occurs
print(f"Occurrences of 'strawberry': {fruit.count("strawberry")}")

# Unpack tuple into variables
first, second, third = fruit 
print(f"{first=}")
print(f"{second=}")
print(f"{third=}")