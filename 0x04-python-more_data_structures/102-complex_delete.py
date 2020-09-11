#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dic_list = [(x, y) for x, y in a_dictionary.items()]
    for i, j in dic_list:
        if j == value:
            del a_dictionary[i]
    return(a_dictionary)
