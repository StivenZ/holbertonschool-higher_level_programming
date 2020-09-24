#!/usr/bin/python3
"""Square class with private instance"""


class Square:
    """Square class with private instance"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Getter method"""
        return (self.size)

    @size.setter
    def size(self, value):
        """Setter method"""
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method to compute the square"""
        return (self.__size ** 2)
