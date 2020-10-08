#!/usr/bin/python3
"""Reads and prints from a file
"""

def read_file(filename=""):
    """Prints to stdout a file's content

    Args:
        filename (str, optional): Name of the file to be read. Defaults to "".
    """

    with open(filename, mode="r", encoding="utf-8") as myfile:
        print(myfile.read())
