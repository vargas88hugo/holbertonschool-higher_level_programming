#!/usr/bin/python3
"""
This module provides Base Class
"""
import json
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Function that saves a json file
        """
        a = []
        if list_objs is not None:
            for i in list_objs:
                a[len(a):] = [i.to_dictionary()]
            j = cls.to_json_string(a)
        else:
            j = cls.to_json_string(list_objs)
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(j)

    @staticmethod
    def from_json_string(json_string):
        """
        Function that returna list of JSON representation
        """
        if not json_string or json_string is None:
            return json.loads("[]")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Function that creates a new instance of the class
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            r1 = cls(1, 1)
        elif cls is Square:
            r1 = cls(1)
        r1.update(**dictionary)
        return r1

    @classmethod
    def load_from_file(cls):
        """
        Function that return a list of instances
        """
        if not os.path.isfile(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", encoding="utf-8") as f:
            a = f.read()
        d = cls.from_json_string(a)
        a = []
        for i in d:
            a[len(a):] = [cls.create(**i)]
        return a
