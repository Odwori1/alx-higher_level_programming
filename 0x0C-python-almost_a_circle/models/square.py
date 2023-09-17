#!/usr/bin/python3
"""Imported modules for the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Rectangle class, inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print format for the square class"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size of square"""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """Helper method to update instance attr using specific keyword args

        Args:
        id (int): New value for the id attribute
        width (int): New value for the width attribute
        height (int): New value for the height attribute
        x (int): New value for the x attribute
        y (int): New value for the y attribute
        """
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Update instance attributes using positional and keyword arguments.

        Args:
        *args: Positional arguments containing attribute values to update
        **kwargs: Keyword arguments containing attribute values to update
        """
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """returns dictionary rep of a Square"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
