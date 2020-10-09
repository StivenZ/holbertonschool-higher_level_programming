#!/usr/bin/python3
"""Checks object's instance
"""


def is_same_class(obj, a_class):
    """Checks isinstance

    Args:
        obj ([class]): Unknown object to be defined
        a_class ([class]): Class to check object from

    Returns:
        [bool]: True or False
    """
    return (type(obj) is a_class)
