#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        string_list = list(my_string)
        for i in string_list:
            if i == 'c' or i == 'C':
                string_list.remove(i)
            else:
                continue
        new_string = "".join(string_list)
    return(new_string)
