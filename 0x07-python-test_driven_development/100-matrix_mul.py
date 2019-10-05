#!/usr/bin/python3
"""
This module provides a matrix_mul function

The function works by multiplying a matrix
"""


def matrix_mul(m_a, m_b):
    """
    This is a function that multiply a matrix

    Args:
        param1 (m_a): first matrix
        param2 (m_b): second matrix

    Raises:
        TypeError: m_a and m_b must be a list
        TypeError: m_a and m_b must be a list of lists
        TypeError: m_a and m_b can't be a empy
        TypeError: m_a and m_b must be a float or integer
        TypeError: m_a and m_b must have the the same size for any list
        ValueError: m_a and m_b can't be multiplied

    Returns:
        the matrix product
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        if len(i) == 0:
            raise ValueError("m_a can't be empty")
    for i in m_b:
        if len(i) == 0:
            raise ValueError("m_b can't be empty")
    for i in m_a:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    n = len(m_a[0])
    for i in m_a:
        if len(i) != n:
            raise TypeError("each row of m_a must be of the same size")
    n = len(m_b[0])
    for i in m_b:
        if len(i) != n:
            raise TypeError("each row of m_b must be of the same size")
    a, b = len(m_a[0]), len(m_b)
    if a != b:
        raise ValueError("m_a and m_b can't be multiplied")

    new = []
    for i in range(len(m_a)):
        tmp = []
        for j in range(len(m_b[0])):
            s = 0
            for k in range(len(m_a[0])):
                s += m_a[i][k] * m_b[k][j]
            tmp.append(s)
        new.append(tmp)

    return new
