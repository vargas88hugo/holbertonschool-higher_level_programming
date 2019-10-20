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
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def update(self, *args, **kwargs):
        if args:
            l = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, l[i], args[i])
        else:
            for i, j in kwargs.items():
                setattr(self, i, j)


    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.size)
