#!/usr/bin/python3
"""
This module provides a matrix_divided function

Basically it is a function for divide that divides a matrix
"""


def matrix_divided(matrix, div):
    """
    This is a function for divide the elements of a matrix

    Args:
       param1 (matrix): list of lists of integers or floats
       param2 (div): integer number for divide

    Raises:
       TypeError: the elements of the matrix must be a integer or float
       TypeError: Each row of the matrix must have the same size
       TypeError: div must be a integer or float number
       ZeroDivisionError: div can't equal to zero

    Returns:
       A new divided matrix
    """
    str1 = "matrix must be a matrix (list of lists) of integers/floats"

    for row in matrix:
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError(str1)
            else:
                col = int(col)

    n = len(matrix[0])
    for row in matrix:
        if len(row) != n:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    a = matrix[:]

    a = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))

    return a
