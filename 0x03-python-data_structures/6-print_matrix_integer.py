#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix[0]:
        print()
    else:
        for a in matrix:
            for idx, l in enumerate(a):
                if idx != len(a) - 1:
                    print("{:d} ".format(l), end='')
                else:
                    print("{:d}".format(l))
