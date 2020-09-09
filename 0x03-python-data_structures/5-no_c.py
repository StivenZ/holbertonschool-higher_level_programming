#!/usr/bin/python3
def no_c(my_string):
    # Struggled trying to find out why the uncommented
    # solution wouldnt work in some cases: we must not
    # change the list in which we are iterating:
    #  back up and iterate over the original, otherwise we may be
    # struggling with index misspositioning.

    # newstr = ""
    # for char in my_string:
    #     if char != 'C' and char != 'c':
    #         mystr += char
    # return newstr

    if my_string:
        string_list = list(my_string)
        for i in list(my_string):
            if i == 'c' or i == 'C':
                string_list.remove(i)
        new_string = "".join(string_list)
    return(new_string)
