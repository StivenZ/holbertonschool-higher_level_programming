#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    for idx, i in enumerate(my_list):
        if i == search:
            new_list[idx] = replace
    return(new_list)
