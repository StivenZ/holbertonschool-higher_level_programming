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
