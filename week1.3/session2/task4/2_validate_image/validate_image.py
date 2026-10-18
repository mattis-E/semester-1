# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except

# Read the file content
fname = input("Filename: ")
file = open("../images/" + fname)

specified_width = 0
specified_height = 0
specified_max_value = 0
valid = True
counter = 0
for line in file:
    ln_list = line.strip().split(" ")
    ln_list[:] = (val for val in ln_list if val != '')

    # ignore first line
    if counter == 0:
        pass
    # record specified width and height
    elif counter == 1:
        specified_width = int(ln_list[0])
        specified_height = int(ln_list[1])
    # record specified max value
    elif counter == 2:
        specified_max_value = int(ln_list[0])
    else:
        # check if width is exceeded
        if len(ln_list) > specified_width:
            valid = False
            print("Invalid width")

        for i in ln_list:
            if i != '':
                i = int(i)
                if i > specified_max_value or i < 0:
                    valid = False
                    print("Invalid pixel values")
        

    counter += 1
    
if counter - 3 < specified_height:
    valid = False
    print("Invalid height")

if valid == True:
    print("Valid image")

# Store the width, the height, and the maximum gray value

# For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive

# Check if the widths and heights are the same as specified

# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value