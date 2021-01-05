#!/usr/bin/python3
"""Module about JSON repr and usage with classes"""


class Student():
    """Define Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs:
            new_dict = {}
            for atr in attrs:
                if atr in self.__dict__:
                    new_dict[atr] = self.__dict__[atr]
            return (new_dict)
        elif attrs is None or attrs == []
            return (self.__dict__)
