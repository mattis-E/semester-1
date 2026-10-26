# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
import geometry

c = geometry.Circle(5, geometry.Point(0, 0))
pY1 = geometry.Point(2, 2)
pY2 = geometry.Point(-2, -2)
pN1 = geometry.Point(6, 2)
pN2 = geometry.Point(6, 6)

print(pY1 in c)
print(pY2 in c)
print(pN1 in c)
print(pN2 in c)