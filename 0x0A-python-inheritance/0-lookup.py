#!/usr/bin/python3
"""Lists attributes and methods
"""


def lookup(obj):
    """[summary]

    Args:
        obj ([class]): It's an instance of a class

    Returns:
        [list]: A list with attributes and methods of the currentoobject
    """
    return (list(dir(obj)))
