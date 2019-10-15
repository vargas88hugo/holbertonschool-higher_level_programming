#!/usr/bin/python3
"""
This module provides add_attribute() function
"""


def add_attribute(obj, name, value):
    """
    This is a function that adds attributes to the object

    Args:
        param1 (obj): object to be added the attribute
        param2 (name): name of the attribute
        param3 (value): value of the attribute
    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")

    return setattr(obj, name, value)
