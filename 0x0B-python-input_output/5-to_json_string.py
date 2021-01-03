#!/usr/bin/python3
"""Module about JSON representation"""
import json


def to_json_string(my_obj):
    """Funtion returns the JSON representation of a string"""
    j = json.dumps(my_obj)
    return (j)
