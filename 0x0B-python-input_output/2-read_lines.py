#!/usr/bin/python3
"""Read n lines at first"""
n = __import__('1-number_of_lines').number_of_lines


def read_lines(filename="", nb_lines=0):
    """Read lines"""

    idx = 0

    count = n(filename)

    with open(filename, "r", encoding="utf-8") as fd:
        if nb_lines >= count or nb_lines <= 0:
            print(fd.read(), end="")
        else:
            for b in fd:
                if idx < nb_lines:
                    print(b, end="")
                idx += 1
