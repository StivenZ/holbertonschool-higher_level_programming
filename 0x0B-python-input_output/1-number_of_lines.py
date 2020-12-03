#!/usr/bin/python3
"""Count number of lines"""


def number_of_lines(filename=""):
    count = 0
    with open(filename, "r", encoding="utf-8") as fd:
        for a in fd:
            count = count + 1
    return count
