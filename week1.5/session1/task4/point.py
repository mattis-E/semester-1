# Week 1.5, Session 1: Task 3
import math

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Add distance() method here
    def distance(self):
        return round(math.sqrt(self.x**2 + self.y**2), 2)

    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self, x, y):
        return round(math.sqrt((x-self.x)**2 + (y-self.y)**2), 2)



# Finally, add code here to demonstrate use of Point
p1 = Point(5, 10)
print(f"Distance from origin: {p1.distance()}")
print(f"Distance from (15, 30): {p1.distance_to(15, 30)}")
