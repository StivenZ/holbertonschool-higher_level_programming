#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    square_list = []
    for i in matrix:
        square_list.append(list(map(lambda x: x ** 2, i)))
    return(square_list)
