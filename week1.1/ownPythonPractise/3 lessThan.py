# Given a list of integers, print its elements that are less than X

hardcoded_list = [1, 5, 8, 10, 12, 19, 29, 3, 4, 30, 35, 41, 6]

def find(condition, limit):
    for n in hardcoded_list:
        if n < limit and condition == 1:
            print(n)
        elif n > limit and condition == 2:
            print(n)
       
greater_or_lesser = int(input("Press 1 to check for numbers LESS THAN x, and 2 for numbers GREATER THAN x: "))
limit = int(input("And now input x: "))

if greater_or_lesser == 1 or greater_or_lesser == 2:
    find(greater_or_lesser, limit)
else:
    print("Illegal input.")
    quit()