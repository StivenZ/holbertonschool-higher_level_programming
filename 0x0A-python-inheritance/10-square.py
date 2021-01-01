#!/usr/bin/python3
"""Empty class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherited from Rectangle
    """
    def __init__(self, size):
        super().__init__(size, size)

    def __str__(self):
        return("[{}] {}/{}".format(self.__class__.__name__,
                                   self.width, self.height))
