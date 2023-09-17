#!/usr/bin/python3
"""Imported modules for the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width of rectangle"""
        self.validate_attribute("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Getter for height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height of rectangle"""
        self.validate_attribute("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        self.validate_attribute("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        self.validate_attribute("y", value)
        self.__y = value

    def validate_attribute(self, name, value, inclusive=True):
        """Function to validate the attribute

        Args:
            name: Name of the attribute to be validated
            value: The attribute value
            inclusive: Bool flag indicating whether the val is inclusive
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if inclusive and value < 0:
            raise ValueError(f"{name} must be >= 0")
        elif not inclusive and value <= 0:
            raise ValueError(f"{name} must be > 0")

    def area(self):
        """Function that returns the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the string representation of a rectangle"""
        rep = '\n' * self.y
        rep += (' ' * self.x + '#' * self.width + '\n') * self.height
        print(rep, end='')

    def __str__(self):
        """Returns string format of rectangle"""
        return '[{}] ({}) {}/{} - {}/{}'.format(
            type(self).__name__, self.id, self.x, self.y,
            self.width, self.height
        )

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

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """Helper method to update instance attr using specific key arg

        Args:
        id (int): New value for the id attribute
        width (int): New value for the width attribute
        height (int): New value for the height attribute
        x (int): New value for the x attribute
        y (int): New value for the y attribute
        """
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def to_dictionary(self):
        """returns dictionary rep of a Rectangle"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
