#!/usr/bin/python3
"""
This module provides a say_my_name function

The function works by printing the name of the user
"""

def say_my_name(first_name, last_name=""):
    """
    This is a function that prints a name

    Args
       param1 (first_name): The first name of the user
       param2 (last_name): The last name of the user

    Raise:
       TypeError: first_name must be a string
       TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}". format(first_name, last_name))
