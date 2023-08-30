#!/usr/bin/python3
"""Class module"""
import math


class MagicClass:
    """MagicClass class"""

    def __init__(self, radius=0):
        """Class constructor"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def circumference(self):
        """This Method returns the circumference

        Returns: The current circumference
        """
        return 2 * math.pi * self.__radius

    def area(self):
        """This Method returns the area

        Returns: The current area
        """
        return self.__radius ** 2 * math.pi
