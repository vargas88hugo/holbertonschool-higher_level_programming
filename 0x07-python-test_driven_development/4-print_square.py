#!/usr/bin/python3
"""
This module provides a print_square function

The function works by printing a square
"""


def print_square(size):
    """
    This is a function that prints a square

    Args
       param1 (size): size of the square

    Raise:
       TypeError: size must be an integer
       ValueError: size must be greater than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()

    for i in range(size):
        k = 0
        for j in range(size):
            print("#", end="")
        if k != size - 1:
            print()
