# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music = {
    "Band1": ["Album1", 1990],
    "Band2": ["Album2", 1991],
    "Band3": ["Album3", 1992]
}

# Pretty-print the data structure
pprint(music)

# Display details of one album recorded by a specific artist
pprint(music.get("Band2"))

# Total number of albums:
print(f"Total number of albums: {len(music)}")