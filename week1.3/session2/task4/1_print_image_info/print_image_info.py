# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

filename = input("Filename: ")
file = open("../images/" + filename)

counter = 0
for line in file:
    if counter == 0:
        pass
    elif counter == 1:
        print("Dimensions: " + line[0:len(line)-1])
    elif counter == 2:
        print("Maximum grey value: " + line[0:len(line)-1])
    elif counter == 3:
        break
    counter += 1


# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)