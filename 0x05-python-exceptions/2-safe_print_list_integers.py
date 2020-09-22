#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print(my_list[i], end='')
                j = j + 1
        print()
        return (j)
    except:
        raise
