# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers()

min = numbers.sort()
print(f"Minimum = {numbers[0]}")

numbers.sort(reverse = True)
print(f"Maximum = {numbers[0]}")

mean = sum(numbers) / len(numbers)
print(f"Mean = {mean}")

median = len(numbers) // 2
median = numbers[median]
print(f"Median = {median}")