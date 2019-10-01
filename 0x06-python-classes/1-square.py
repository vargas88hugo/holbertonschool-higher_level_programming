#!/usr/bin/python3
"""
Module of the class square
"""
class Square:
    """
    This is a class for define a private instance attribute.

    Attributes:
       attr1 (size): size of the square.
    """
    def __init__(self, size):
        """
        The constructor for Square class.

        Args:
           param1 (size): size of the square
        """
        self.__size = size
