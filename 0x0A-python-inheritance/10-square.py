#!/usr/bin/python3
"""
This module provides Square Class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square Class
    """
    def __init__(self, size):
        """
        Constructor of the class
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
