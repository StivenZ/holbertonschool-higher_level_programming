#!/usr/bin/python3
"""Empty class about squares"""


class Square:
    """Empty class about squares"""
    def __init__(self, size=0):
        self.__size = size
        if not type(size) is int:
            raise TypeError("size most be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
