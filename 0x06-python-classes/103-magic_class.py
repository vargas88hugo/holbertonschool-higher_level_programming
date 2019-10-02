#!/usr/bin/python3
class MagicClass:
    """
    This is a class of MagicClass

    Attributes
       attrb1
    """
    def __init__(self, radius=0):
        self.__radius = radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ function area """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ function circumference"""
        return (2 * math.pi * self.__radius)
