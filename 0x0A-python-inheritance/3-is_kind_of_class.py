#!/usr/bin/python3
"""Checks if object is instance of class or subclass
"""


def is_kind_of_class(obj, a_class):
    """Checks if is instance or subclass

    Args:
        obj ([any]): object of any type
        a_class ([type]): type to be compared to

    Returns:
        [boolean]: True or False
    """
    return (isinstance(obj, a_class))
