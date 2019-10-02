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

    @property
    def position(self):
        return self__position

    @position.setter
    def position(self, position):
        if type(position) == tuple and len(position) == 2 and \
           type(position[0]) == int and type(position[1]) == int \
           and position[0] >= 0 and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        for i in range(self.__position[1]):
            print()
        if self.__size == 0:
            print("{}".format(" " * self.position[0]))
        for i in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
