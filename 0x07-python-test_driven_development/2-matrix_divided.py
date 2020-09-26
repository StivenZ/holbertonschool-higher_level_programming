#!/usr/bin/python3
"""Divides Matrix
"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix (list): list of lists
        div (int or float): diviosr

    Raises:
        TypeError: For non int or float, nor empty lists of lists
        ZeroDivisionError: [description]

    Returns:
        [Matrix]: New dividex matrix
    """

    check_row = []
    copy_matrix = []

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    for i, row in enumerate(matrix):
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        if len(check_row) != 0:
            if len(row) not in check_row:
                raise TypeError("Each row of the matrix must \
have the same size")
        copy_matrix.append([])
        check_row.append(len(row))
        for j, item in enumerate(row):
            if type(item) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
            copy_matrix[i].append(round((matrix[i][j] / div), 2))
    return (copy_matrix)
