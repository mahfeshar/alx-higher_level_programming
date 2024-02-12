#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Give width and height to rectangle

        Args:
            width (int): The width for rectangle. Defaults to 0.
            height (int): The height for rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Returns a visual representation of the Rectangle object.

        Args:
            self (Rectangle): The Rectangle object to be visualized.

        Returns:
            str: A visual representation of the Rectangle object.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        vis = []
        for i in range(self.__height):
            [vis.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                vis.append("\n")
        return ("".join(vis))

    def __repr__(self):
        """Return a string representation of the Rectangle object.

        Returns:
            str: A string representation of the Rectangle object.
        """
        rectan = "Rectangle(" + str(self.__width)
        rectan += ", " + str(self.__height) + ")"
        return (rectan)

    def __del__(self):
        """destructor for the class"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @property
    def width(self):
        """Getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width"""
        if not (isinstance(value, int)):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return the area of the Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the periemter of the rectangle"""
        if self.__width == 0 or self.height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the bigger of two Rectangles.

        Args:
            rect_1 (Rectangle): The first Rectangle to compare.
            rect_2 (Rectangle): The second Rectangle to compare.

        Returns:
            Rectangle: The bigger of the two Rectangles.

        Raises:
            TypeError: If either argument is not a Rectangle.

        """
        if not (isinstance(rect_1, Rectangle)):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not (isinstance(rect_2, Rectangle)):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        Creates a square instance of the Rectangle class.

        Args:
            size (int): The length of the side of the square. Defaults to 0.

        Returns:
            Rectangle: A square instance of the Rectangle class.
        """
        return (cls(size, size))
