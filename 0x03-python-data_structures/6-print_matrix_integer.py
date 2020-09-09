#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for a in matrix:
            for idx, l in enumerate(a):
                if idx != len(a) - 1:
                    print("{:d}, ".format(l), end='')
                else:
                    print("{}".format(l))
