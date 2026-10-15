# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file
inp = ""
num_spaces = 0
while True:
    inp = input("filename: ")
    if (inp == "quit"):
        break
    with open(inp, "r") as file:
        for line in file:
            if len(line) > 1:
                num_spaces += line.count(" ") + line.count("\n")

    #print(f"Length of {inp}: {str.count(" ") + str.count("\n")}")
    print(num_spaces + 1)
    num_spaces = 0



# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210