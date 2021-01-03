#!/usr/bin/python3
"""Module to append string into a file"""


def append_write(filename="", text=""):
    """Append a string into a file"""

    with open(filename, "a", encoding="utf-8") as fd:
        n = fd.write(text)

    return (n)
