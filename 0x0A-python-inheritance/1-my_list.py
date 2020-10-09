#!/usr/bin/python3
"""Prints sorted list
"""


class MyList(list):
    """Class list

    Args:
        list ([list]): retreives sorted list
    """

    def print_sorted(self):
        new = self.copy()
        new.sort()
        print(new)
