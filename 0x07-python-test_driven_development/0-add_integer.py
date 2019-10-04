#!/usr/bin/python3
"""
This module provides a add_integer function.

The arguments of the function are integers values and the result is its sum
"""


def add_integer(a, b=98):
    """
    This is a function for adds two integers

    Args:
       param1 (a): first number
       param2 (b): second number

    Raises:
       TypeError: the arguments must be integers or floats

    Returns:
       The sum of the two numbers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    else:
        a = int(a)
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        b = int(b)

    return (a + b)
