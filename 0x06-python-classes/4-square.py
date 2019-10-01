#!/usr/bin/python3


class Square:
    """
    This is a class for define a private instance attribute.

    Attributes:
       attr1 (size): size of the square.
    """
    def __init__(self, size=0):
        """
        The constructor for Square Class

        Args:
           param1 (size): size of the square

        Raises:
           ValueError: If size is less than zero
           TypeError: If size is not a integer
        """
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        """
        This is a getter of the class
        """
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Function that calculates the area of the square

        Returns:
           Area of the square
        """
        return self.__size * self.__size
