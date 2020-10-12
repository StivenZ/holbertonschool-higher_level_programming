#!/usr/bin/python3
"""Rectangle subclass
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class

    Args:
        Base ([Base]): Inherited class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.___width = width
        self.___height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return (self.___width)

    @width.setter
    def width(self, value):
        self.___width = value

    @property
    def height(self):
        return (self.___height)

    @height.setter
    def height(self, value):
        self.___height = value

    @property
    def x(self):
        return (self.___x)

    @x.setter
    def x(self, value):
        self.___x = value

    @property
    def y(self):
        return (self.___y)

    @y.setter
    def y(self, value):
        self.___y = value
