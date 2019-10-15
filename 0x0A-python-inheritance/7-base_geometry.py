#!/usr/bin/python3
"""
This module provides BaseGeometry class
"""


class BaseGeometry():
    """
    BaseGeometry Class
    """
    def area(self):
        """
        function that raises an error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that raises an error if the condition is not fulfilled
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
