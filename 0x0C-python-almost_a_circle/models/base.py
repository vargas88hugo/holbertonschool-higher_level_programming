#!/usr/bin/python3
"""
This module provides Base Class
"""


class Base:
    """
    This is a base class of the project

    Attributes:
        attr1 (id): id of the class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor of the class
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
