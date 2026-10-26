# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("Width or height are not integer types!")
        if width <= 0 or height <= 0:
            raise ValueError("Width or height are less than 0!")
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    def is_square(self):
        """is_square
        args: none
        returns: boolean.
        if the rectangle is a square (has equal width and height), true is returned.
        otherwise, false is returned.
        """
        if self.width == self.height:
            return True
        return False

    def area(self):
        """area
        args: none
        returns: integer
        returns the area of the rectangle.
        """
        return self.width * self.height 

    def perimeter(self):
        """perimeter
        args: none
        returns: integer
        returns the perimiter of the rectangle.
        """
        return (2 * self.width) + (2 * self.height)
    # (See README.md for details of what they should do)