#!/usr/bin/python3
"""
This module provides is_kind_of_class(obj, a_class) function
"""


def is_kind_of_class(obj, a_class):
    """
    This is a function that returns True if is a exactly instance or False

    Args:
        param1 (obj): object to be checked
        param2 (a_class): class to be checked

    Returns:
        True if the object is a instance of the clase or False otherwise
    """
    return isinstance(obj, a_class)
