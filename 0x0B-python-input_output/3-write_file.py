#!/usr/bin/python3
"""Module used to write to a given file"""



def write_file(filename="", text=""):
    """Write certain text onto a file"""

    with open(filename, "w", encoding="utf-8") as fd:
        n = fd.write(text)

    return (n)
