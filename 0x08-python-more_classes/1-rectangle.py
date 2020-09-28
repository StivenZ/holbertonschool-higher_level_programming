#!/usr/bin/python3
"""Rectangle class
"""


class Rectangle:
    """Generates an empty rectangle.
    """
    def __init__(self, width=0, heigth=0):
        self.__width = width
        self.__heigth = heigth
    
    @property
    def width(self):
        return (__width)

    @width.setter
    def width(self, value):
        if type(value) not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return (__heigth)

    @height.setter
    def height(self, value):
        if type(value) not int:
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
