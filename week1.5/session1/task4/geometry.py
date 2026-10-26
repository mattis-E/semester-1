# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math
import point

# Copy Point class definition here

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle
class Circle:
    def __init__(self, centre: point, radius):
        self.centre = centre
        self.radius = radius

    def area(self):
        return round((math.pi * self.radius**2), 2)

    def perimeter(self):
        return round(math.pi * self.radius * 2, 2)

# Don't add any testing code to this file!
