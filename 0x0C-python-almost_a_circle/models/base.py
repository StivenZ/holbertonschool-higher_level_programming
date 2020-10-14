#!/usr/bin/python3
import json
"""Base class
"""


class Base:
    """Base clase
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Turns json to string
        """
        if list_dictionaries == None or list_dictionaries == {}:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves json to a file
        """
        if list_objs == None:
            vary = "[]"
        else:
            vary = cls.to_json_string([i.to_dictionary() for i in list_objs])
        filename = cls.__name__ + ".json"

        with open(filename, mode="w", encoding="UTF-8") as _file:
            _file.write(vary)
