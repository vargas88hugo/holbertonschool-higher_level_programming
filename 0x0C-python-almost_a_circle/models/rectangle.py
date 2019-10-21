#!/usr/bin/python3
"""
This module provides Rectangle Class
"""
from models.base import Base


class Rectangle(Base):
    """
    This is a rectangle class of the project

    Attributes:
        attr1 (width): width of the rectangle
        attr2 (height): height of the rectangle
        attr3 (x): x axes
        attr4 (y): y axes
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor of the class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        function that returns the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Function that prints a picture representation of the rectangle
        """
        str1 = ""
        for i in range(self.__y):
            str1 += "\n"
        for i in range(self.__height):
            for k in range(self.__x):
                str1 += " "
            for j in range(self.__width):
                str1 += "#"
            str1 += "\n"
        print(str1[:-1])

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """
        Function that updates the attributes of the rectangle
        """
        if args:
            li = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, li[i], args[i])
        else:
            for i, j in kwargs.items():
                setattr(self, i, j)

    def to_dictionary(self):
        """
        Function that returns a dictionary representation
        """
        d = {}
        for i, j in self.__dict__.items():
            if i == "id":
                d["id"] = j
            elif i == "_Rectangle__width":
                d["width"] = j
            elif i == "_Rectangle__height":
                d["height"] = j
            elif i == "_Rectangle__x":
                d["x"] = j
            elif i == "_Rectangle__y":
                d["y"] = j
        return d
