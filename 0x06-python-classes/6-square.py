#!/usr/bin/python3
class Square:
    """
    Class of Square

    Attributes:
       attr1 (size): size of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor of the class

        Args:
           param1 (size): size of the square
           param2 (position): tuple coordinates of the initial position

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

        if type(position) is tuple and len(position) is 2 and \
           type(position[0]) is int and type(position[1]) is int \
           and position[0] >= 0 and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """
        This is a getter of the class
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Function that calculates the area of the square

        Returns:
           Area of the square
        """
        return self.__size * self.__size

    @property
    def position(self):
        return self__position

    @position.setter
    def position(self, value):
        if type(value) == tuple and len(value) == 2 and \
           type(value[0]) == int and type(value[1]) == int \
           and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
        Function that prints the area of the square
        """
        if self.__size == 0:
            print()
            return

        str1 = ""

        for i in range(self.__position[1]):
            str1 += "\n"

        for n in range(self.__size):
            for j in range(self.__position[0]):
                str1 += " "
            for k in range(self.__size):
                str1 += "#"
            str1 += "\n"
        str1 = str1[:len(str1) - 1]
        print(str1)
