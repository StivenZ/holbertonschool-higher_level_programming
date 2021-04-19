#!/usr/bin/python3
"""Adds new attributes when possible
"""

def add_attribute(instance, attr_name, attr_value):
    """Checks for primitive types to set attributes"""
    primitives = [str, int, bool, tuple, list, set]
    if type(instance) not in primitives:
        setattr(instance, attr_name, attr_value)
    else:
        raise Exception("can't add new attribute")
