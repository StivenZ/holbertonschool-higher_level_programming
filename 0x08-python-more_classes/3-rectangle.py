#!/usr/bin/python3
"""Rectangle class
"""


class Rectangle:
    """Generates an empty rectangle.
    """
    def __init__(self, width=0, heigth=0):
        if type(heigth) is not int:
            raise TypeError("heigth must be an integer")
        if heigth < 0:
            raise ValueError("heigth must be >= 0")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        self.__heigth = heigth

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
        return (self.__heigth)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__heigth = value

    def area(self):
        return (self.__heigth * self.__width)

    def perimeter(self):
        if (self.__width or self.__heigth) == 0:
            return (0)
        else:
            return ((self.__width * 2) + (self.__heigth * 2))

    def __str__(self):
        sqr = ""
        for i in range(self.__heigth):
            sqr = sqr + ("#" * self.__width) + "\n"
        return (sqr)
