#!/usr/bin/python3
class Square:
    """
    This is a class for define a print square

    Attributes:
       attr1 (size): size of the square
    """
    def __init__(self, size=0):
        """
        The constructor for Square Class

        Args:
           param1 (size): size of the square
        """
        self.size = size

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

    def my_print(self):
        """
        Function that prints the area of the square
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("{}".format("#" * self.__size))
