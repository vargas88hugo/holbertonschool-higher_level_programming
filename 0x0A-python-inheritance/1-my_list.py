#!/usr/bin/python3
"""
This module provides a MyList Class
"""


class MyList(list):
    """
    Class of MyList

    Attributes:
        attr1 (list): object list
    """
    def __init__(self):
        """
        Constructor of the class
        """
        super().__init__()

    def print_sorted(self):
        """
        Function that prints a sorted list
        """
        a = self
        a = sorted(a)
        print(a)
