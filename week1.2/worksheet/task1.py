# Worksheet 1.2: Task 1 Solution
import sys

try:
    num = int(input("Enter an integer grade (0 - 100): "))
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if num < 0 or num > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if 0 <= num <= 39:
    print(f"{num} is a Fail")
elif 40 <= num <= 69:
    print(f"{num} is a Pass")
elif 70 <= num <= 100:
    print(f"{num} is a Distinction")
