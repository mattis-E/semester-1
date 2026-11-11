# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle

from geometry import Point, Circle

"""
Test whether the constructor works properly
"""
def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

# Test whether the distances between two points are calculated correctly
def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0
    
# test whether the distance from one point to another is calculated correctly
def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(5, 0)
    assert p1.distance_to(p2) == 5

# test the constructor of circles with different cases.
def test_init():
    p1 = Circle(0, Point(0, 0))
    assert p1.centre.x == 0 and p1.centre.y == 0 and p1.radius == 0

    p2 = Circle(1, Point(-5, 4))
    assert p2.centre.x == -5 and p2.centre.y == 4 and p2.radius == 1

    p3 = Circle(3, Point(10.5, -5))
    assert p3.centre.x == 10.5 and p3.centre.y == -5 and p3.radius == 3

# test the circle's area() function, which returns the area of the circle.
def test_area():
    c1 = Circle(5, Point(2, 2))
    assert 78.4 < c1.area() < 78.6

# test whether the perimeter of a circle is correctly calculated.
def test_perimeter():
    c1 = Circle(5, Point(2, 2))
    assert 31.4 < c1.perimeter() < 31.5