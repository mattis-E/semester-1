# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

from geometry import Circle
from point import Point


# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
circle_centre = Point(5, 5)
#  - Creates a Circle object, using the Point object and a value for radius
circle = Circle(circle_centre, 5)

#  - Displays the area of the circle
print(f"Area: {circle.area()}")
#  - Displays the perimeter of the circle
print(f"Perimetre: {circle.perimeter()}")