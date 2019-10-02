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
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

        if type(position) is not tuple or len(position) != 2 or \
           type(position[0]) != int or type(position[1]) != int \
           or position[0] < 0 and position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """
        This is a getter of the class
        """
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """
        Function that calculates the area of the square

        Returns:
           Area of the square
        """
        return self.__size ** 2

    @property
    def position(self):
        return self__position

    @position.setter
    def position(self, position):
        if type(position) is not tuple or len(position) != 2 or \
           type(position[0]) != int or type(position[1]) != int \
           or position[0] < 0 and position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def my_print(self):
        """
        Function that prints the area of the square
        """
        if self.__size == 0:
            print()
            return

        str1 = ""

        str1 += ("\n" * self.__position[1])

        for i in range(self.__size):
            str1 += (" " * self.__position[0])
            str1 += ("#" * self.__size)
            str1 += "\n"
        str1 = str1[:len(str1) - 1]
        print(str1)

    def __str__(self):
        """
        Function that prints the area of the square
        """
        if self.__size == 0:
            return "\n"

        str1 = ""

        for i in range(self.__position[1]):
            str1 += "\n"

        for i in range(self.__size):
            for j in range(self.__position[0]):
                str1 += " "
            for j in range(self.__size):
                str1 += "#"
            str1 += "\n"
        str1 = str1[:len(str1) - 1]
        return str1
