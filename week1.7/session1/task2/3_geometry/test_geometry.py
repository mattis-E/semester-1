# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle

from geometry import Point, Circle

def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0
    
def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    
    # complete the implementation for
    # testing distance_to()
def test_distance_to():
    p1 = Point(0, 0)
    p2 = Point(5, 0)
    assert p1.distance_to(p2) == 5

def test_init():
    p1 = Circle(0, Point(0, 0))
    assert p1.centre.x == 0 and p1.centre.y == 0 and p1.radius == 0

    p2 = Circle(1, Point(-5, 4))
    assert p2.centre.x == -5 and p2.centre.y == 4 and p2.radius == 1

    p3 = Circle(3, Point(10.5, -5))
    assert p3.centre.x == 10.5 and p3.centre.y == -5 and p3.radius == 3
def test_area():
    c1 = Circle(5, Point(2, 2))
    assert 78.4 < c1.area() < 78.6
def test_perimeter():
    c1 = Circle(5, Point(2, 2))
    assert 31.4 < c1.perimeter() < 31.5

# Write test functions to test the __init__(), 
# area() and perimeter() methods in Circle class
# you can use the default value for centre coordinates
