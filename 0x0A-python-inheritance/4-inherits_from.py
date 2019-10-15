#!/usr/bin/python3
"""
This module provides inherits_from(obj, a_class) function
"""


def inherits_from(obj, a_class):
    """
    This is a function that returns True if is a instance or False

    Args:
        param1 (obj): object to be checked
        param2 (a_class): class to be checked

    Returns:
        True if the object is a instance of the clase or False otherwise
    """
    return (isinstance(obj, a_class) and obj.__class__ != a_class)
