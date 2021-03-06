#!/usr/bin/python3
"""Square class with private instance"""


class Square:
    """Square class with private instance"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] < 0) or (position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        return ()

    def my_print(self):
        # times = self.__size * "#"
        print("\n" * self.__position[1], end='')
        if self.__size != 0:
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
        else:
            print()
