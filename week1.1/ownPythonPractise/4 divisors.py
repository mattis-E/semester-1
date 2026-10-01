import math

num = int(input("Enter a number: "))
check = input("Print non-factors? Y/N: ").lower()

for i in range(1, num):
    if num % i == 0:
        print(f"{i} is a factor.")
    elif num % i != 0 and check == "y":
        print(f"{i} is not a factor.")