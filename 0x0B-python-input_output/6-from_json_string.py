#!/usr/bin/python3
"""Module dealing with JSON serializations and deserializations"""
import json


def from_json_string(my_str):
    """Return an object from a json file"""
    j = json.loads(my_str)
    return (j)
