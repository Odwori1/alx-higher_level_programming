#!/usr/bin/python3
"""Write imported module here"""


class BaseGeometry:
    """The BaseGeometry class"""
    def area(self):
        """Func that calculate area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Func that validate value

        Args:
        name: name of int
        value: value of int

      Raises:
            TypeError: if value is not an integer
            ValueError: if value is  less than 0
        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
