
# function implementation

def rectangle_area(width, height):  # define suitable input data
    return width * height

def get_even_sequence(max):
    lst = []
    for i in range (0, max):
        if i % 2 == 0:
            lst.append(i)
    return lst

def get_mean(lst):
    return sum(lst) / len(lst)

print(f"Area is {rectangle_area(5, 10)}")   # provide suitable data matching your inputs
print(f"Even integers between 0 and 15: {get_even_sequence(15)}")
print(f"Mean of a list: {get_mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}")
