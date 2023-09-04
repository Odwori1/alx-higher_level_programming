#!/usr/bin/python3
"""Square class module"""


class Square:
    """This is a class Square that defines a square"""

    def __init__(self, size=0):
        """Class constructor

        Args:
            size: the size of the square
        """
        self.__size = size

    @property
    def size(self):
        """This getter func returns the size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This getter func returns the size of the square

        Args:
            value: value to set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This Method returns the area of square

        Returns: The current square area
        """
        return self.__size ** 2

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
