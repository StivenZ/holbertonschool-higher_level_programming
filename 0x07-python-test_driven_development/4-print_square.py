#!/usr/bin/python3
"""Square class with private instance"""


def print_square(size):
    """Square class with private instance"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if size != 0:
        for i in range(size):
            print("#" * size)
