#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = list(str)
    if n < len(str) and n >= 0:
        new_str.remove(str[n])
    return ("".join(new_str))
