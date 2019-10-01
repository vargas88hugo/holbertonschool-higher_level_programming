#!/usr/bin/python3


class Square:
    """
    This is a class for define a private instance attribute.

    Attributes:
       attr1 (size): size of the square.
    """
    def __init__(self, size=0):
        """
        The constructor for Square class.

        Args:
           param1 (size): size of the square

        Raises:
           ValueError: if size is less than zero
           Typeerror: if size is not a integer
        """
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
