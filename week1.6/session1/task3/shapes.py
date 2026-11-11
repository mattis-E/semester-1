# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")

        self.colour = colour


# Implement your Circle class here
# Make sure that it inherits properly from Shape!
class Circle(Shape):
    """
    constructor for the circle, inheriting from Shape.
    """
    def __init__(self, rd, pos, col="red"):
        if isinstance(rd, int) or isinstance(rd, float):
            if rd > 0:
                self.set_radius(rd)
            else:
                raise ValueError("Radius is less than or equal to zero.")
        else:
            raise TypeError("Radius is not an integer or float.")
        self.position = pos
        self.colour = col

    def set_radius(self, rd):
        """
        return the radius of the circle.
        """
        self.radius = rd

    def __str__(self):
        """
        print the circle.
        """
        return f"{self.colour} circle, radius {self.radius}, at {self.position}"

    def area(self):
        """
        return the area of the circle.
        """
        return math.pi * (self.radius**2)
    
    def perimeter(self):
        """
        return the perimeter of the circle.
        """
        return math.pi * self.radius * 2