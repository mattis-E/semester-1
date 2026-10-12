# Week 1.3, Session 1: Task 6b

def cheating(n):
    if n % 2 == 0:
        return 2 * n
    else:
        return n

values = [1,4,2,6,3,7]

print(values)

newval = []
for i in values:
    if i % 2 == 0:
        newval.append(2 * i)
    else:
        newval.append(i)

print(newval)

# write the list comprehension equivalent to the `for` loop
#sval = [cheating(i) for i in values]
sval = [i for i in values]
print(sval)