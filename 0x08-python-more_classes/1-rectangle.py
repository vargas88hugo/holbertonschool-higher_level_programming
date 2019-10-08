#!/usr/bin/python3
"""
This module provides a Rectange class
"""


class Rectangle:
    """
    Class of Rectangle

    Attributes:
        attr1 (width): width of the rectangle
        attr2 (height): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Constructor of the class

        Args:
            param1 (width): width of the rectangle
            param2 (height): height of the rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        This is a getter of the class
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This is a setter of the class
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        This is a getter of the class
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This is a setter of the class
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
