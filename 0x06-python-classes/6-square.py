#!/usr/bin/python3
"""Square class module"""


class Square:
    """This is a class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Class constructor

        Args:
            size: the size of the square
            position: coordinates of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """This getter func returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """This setter func returns the size of the square

        Raises:
          TypeError: if size is not an integer
          ValueError: if size is < 0

        Args:
           value: value to set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """property of the coordinates of this Square

        Raises:
            TypeError: if value != a tuple of 2 integers < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of this Square

        Args: value as a tuple of two positive integers

        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This Method returns the area of square

        Returns: The current square area
        """
        return self.__size**2

    def my_print(self):
        """This Method prints the area of square with the char #"""
        print(self.char_print(), end="")

    def char_print(self):
        """Method that returns the position in spaces"""
        result = ""
        if self.size == 0:
            return "\n"
        for _ in range(self.position[1]):
            result += "\n"

        for _ in range(self.size):
            for _ in range(self.position[0]):
                result += " "
            for _ in range(self.size):
                result += "#"
            result += "\n"
        return result
