#!/usr/bin/python3
"""Module about JSON serializaiton into a file"""
import json


def save_to_json_file(my_obj, filename):
    """Save a json file into a file"""
    with open(filename, "a", encoding="utf-8") as fd:
        json.dump(my_obj, fd)
