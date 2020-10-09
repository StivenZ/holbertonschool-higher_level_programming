#!/usr/bin/python3
"""Checks if subclass or not
"""


def inherits_from(obj, a_class):
    """Checks if subclass

    Args:
        obj ([class]): Oject to check its class
        a_class ([class or type]): Class or type to check against

    Returns:
        [boolean]: True or False
    """
    if type(obj) is a_class:
        return (False)
    else:
        return (issubclass(type(obj), a_class))
