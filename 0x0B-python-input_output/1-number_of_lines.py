#!/usr/bin/python3
"""Count number of lines"""


def number_of_lines(filename=""):
    """Opens a file and reads number of liens"""
    with open(filename, "r", encoding="utf-8") as fd:
        lines = fd.readlines()
    return (len(lines))
