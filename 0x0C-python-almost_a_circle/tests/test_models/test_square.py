#!/usr/bin/python3
"""Imported module for Rectangle tests class"""
import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    def setUp(self):
        """This method is called before each test method"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """This method is called after each test method"""
        pass

    def test_constructor(self):
        """Test constructor"""
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_size_getter_setter(self):
        """Test size getter and setter"""
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_inheritance(self):
        """Test if Square inherits from Rectangle"""
        square = Square(5)
        self.assertIsInstance(square, Rectangle)

    def test_update_args(self):
        """Test update method with positional arguments"""
        square = Square(5)
        square.update(2, 9, 4, 1)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 9)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 1)

    def test_update_kwargs(self):
        """Test update method with keyword arguments"""
        square = Square(5)
        square.update(id=3, size=5, x=8, y=1)
        self.assertEqual(square.id, 3)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 1)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()
        expected_dict = {"id": 1, "size": 5, "x": 2, "y": 3}
        self.assertEqual(square_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
