#!/usr/bin/python3
"""Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class

    Args:
        Rectangle ([class]): class from which it inherited
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        if len(args) >= 1:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                if key in ["id", "size", "x", "y"]:
                    setattr(self, key, value)

    def to_dictionary(self):
        new_dict = {'x': self.x,
                    'y': self.y,
                    'id': self.id,
                    'size': self.width}
        return (new_dict)
