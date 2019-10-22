#!/usr/bin/python3
"""
This module provides Square Class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is a square class of the project

    Attributes:
        attr1 (size): size of the square
        attr3 (x): x axes
        attr4 (y): y axes
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor of the square class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        """
        Function that updates the attributes of the square
        """
        if args:
            li = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, li[i], args[i])
        else:
            for i, j in kwargs.items():
                setattr(self, i, j)

    def to_dictionary(self):
        """
        Function that return a dictionary representation
        """
        d = {}
        for i, j in self.__dict__.items():
            if i == "id":
                d["id"] = j
            elif i == "_Rectangle__height":
                d["size"] = j
            elif i == "_Rectangle__x":
                d["x"] = j
            elif i == "_Rectangle__y":
                d["y"] = j
        return d
