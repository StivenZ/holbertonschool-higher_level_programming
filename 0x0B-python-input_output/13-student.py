#!/usr/bin/python3
"""Module about JSON repr and usage with classes"""


class Student():
    """Define Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            new_dict = {}
            for atr in attrs:
                if atr in self.__dict__:
                    new_dict[atr] = self.__dict__[atr]
            return (new_dict)
        elif attrs is None:
            return (self.__dict__)

    def reload_from_json(self, json):
        self.__dict__.update(json)
