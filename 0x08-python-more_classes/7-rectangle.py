#!/usr/bin/python3
"""Rectangle class
"""


class Rectangle:
    """Generates an empty rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if (self.__width or self.__height) == 0:
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        sqr = ""
        if self.__width == 0 or self.__height == 0:
            return (sqr)
        for i in range(self.__height):
            if i != (self.__height - 1):
                sqr = sqr + (str(self.print_symbol) * self.__width) + "\n"
            else:
                sqr = sqr + (str(self.print_symbol) * self.__width)
        return (sqr)

    def __repr__(self):
        return (type(self).__name__ +
                "({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances += -1
