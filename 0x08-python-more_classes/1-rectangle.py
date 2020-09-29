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