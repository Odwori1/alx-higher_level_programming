#!/usr/bin/python3
"""Module for Rectangle, inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The class rectangle, inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Constructor method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Func that cal the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """func to return the rec description"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
