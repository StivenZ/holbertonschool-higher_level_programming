#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and not matrix[0]:
        print("")
    elif matrix:
        for a in matrix:
            for idx, l in enumerate(a):
                if idx != len(a) - 1:
                    print("{:d}, ".format(l), end='')
                else:
                    print("{:d}".format(l))
