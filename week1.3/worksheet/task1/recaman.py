# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
sequence = []

if len(sequence) == 0:
    sequence.append(0)

for k in range (1, L):
    if sequence[k-1] - k > 0 and sequence[k-1] - k not in sequence:
        sequence.append(sequence[k-1] - k)
    else:
        sequence.append(sequence[k-1] + k)


# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence