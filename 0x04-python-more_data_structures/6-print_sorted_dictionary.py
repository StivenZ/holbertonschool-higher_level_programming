#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered_keys = sorted(a_dictionary.keys())
    for i in ordered_keys:
        print("{}: {}".format(i, a_dictionary[i]))
