#!/usr/bin/python3
"""Square class with private instance"""


class Square:
    """Square class with private instance"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        # times = self.__size * "#"
        if self.__size != 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print()
