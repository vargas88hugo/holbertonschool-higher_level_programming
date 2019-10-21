#!/usr/bin/python3
"""
This module provides Base Class
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Function that returns a json representation
        """
        if not list_dictionaries or list_dictionaries is None:
            return json.dumps([])
        return json.dumps(list_dictionaries)
