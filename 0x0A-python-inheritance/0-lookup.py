#!/usr/bin/python3
"""
This module provides lookup(obj) function
"""


def lookup(obj):
    """
    This is a function that returns the list of available attributes

    Args:
        param1 (obj): object to be checked

    Returns:
        A list of the availabe attributes in the object
    """
    return dir(obj)
