# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)

from shapes import Shape, Circle
from point import Point

"""
test the functionality of the circle class
"""
test = Circle(5, Point(5, 5), "blue")
print(test)
print(f"area: {test.area():.2f}, perimeter: {test.perimeter():.2f}")
test.set_position(Point(3, 3))
print(f"Modified circle: {test}")
test.set_colour("green")
print(f"Modified circle: {test}")