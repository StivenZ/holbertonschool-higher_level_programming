#!/usr/bin/python3
"""Adds two integers
"""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a ([type]): [description]
        b (int, optional): [description]. Defaults to 98.

    Raises:
        TypeError: [description]
        TypeError: [description]

    Returns:
        [type]: [description]
    """
    if a is None or (type(a) not in [int, float]):
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if (type(a) or type(b)) == float:
        a = int(a)
        b = int(b)

    return int(a + b)
