#!/usr/bin/python3
"""Base class
"""
import json


class Base:
    """Base clase
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Turns json to string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves json to a file
        """
        if list_objs is None:
            vary = []
        else:
            vary = cls.to_json_string([i.to_dictionary() for i in list_objs])
        filename = cls.__name__ + ".json"

        with open(filename, mode="w", encoding="UTF-8") as _file:
            _file.write(vary)

    @staticmethod
    def from_json_string(json_string):
        """turns to string from json
        Args:
            json_string ([type]): [description]

        Returns:
            [type]: [description]"""
        if json_string is None or len(json_string) == 0:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance from a dictionary"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls.__name__ == "Square":
            dummy = Square(1)
        elif cls.__name__ == "Rectangle":
            dummy = Rectangle(1, 1)
        else:
            return
        dummy.update(**dictionary)
        return(dummy)
