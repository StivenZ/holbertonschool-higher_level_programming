#!/usr/bin/python3
"""Module to convert JSON object to python object"""
import json


def load_from_json_file(filename):
    """convert json file to python object"""
    with open(filename, "r", encoding="utf-8") as fd:
        j = json.load(fd)

    return (j)
