#!/usr/bin/python3
"""Imported module for Rectangle tests class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from unittest.mock import patch

class TestRectangle(unittest.TestCase):
    def setUp(self):
        """This method is called before each test method"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """This method is called after each test method"""
        pass

    def test_constructor_with_id(self):
        """Test constructor with id"""
        obj = Rectangle(5, 3, 2, 1, 10)
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 3)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 1)
        self.assertEqual(obj.id, 10)

    def test_constructor_without_id(self):
        """Test constructor without id"""
        obj = Rectangle(5, 3, 2, 1)
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 3)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 1)
        self.assertIsInstance(obj.id, int)

    def test_instantiations(self):
        """Test other instances"""
        rect = Rectangle(10, 20)
        self.assertEqual(str(type(rect)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(rect, Base))
        d = {'_Rectangle__height': 20, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(rect.__dict__, d)

        with self.assertRaises(TypeError) as e:
            rect = Rectangle("1", 2)
        message = "width must be an integer"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(TypeError) as e:
            rect = Rectangle(1, "2")
        message = "height must be an integer"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(TypeError) as e:
            rect = Rectangle(1, 2, "3")
        message = "x must be an integer"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(TypeError) as e:
            rect = Rectangle(1, 2, 3, "4")
        message = "y must be an integer"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(ValueError) as e:
            rect = Rectangle(-1, 2)
        message = "width must be > 0"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(ValueError) as e:
            rect = Rectangle(1, -2)
        message = "height must be > 0"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(ValueError) as e:
            rect = Rectangle(0, 2)
        message = "width must be > 0"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(ValueError) as e:
            rect = Rectangle(1, 0)
        message = "height must be > 0"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(ValueError) as e:
            rect = Rectangle(1, 2, -3)
        message = "x must be >= 0"
        self.assertEqual(str(e.exception), message)

        with self.assertRaises(ValueError) as e:
            rect = Rectangle(1, 2, 3, -4)
        message = "y must be >= 0"
        self.assertEqual(str(e.exception), message)


    def test_getters_and_setters(self):
        """Test getters and setters"""
        obj = Rectangle(5, 3, 2, 1)
        obj.width = 10
        obj.height = 7
        obj.x = 3
        obj.y = 2

        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 7)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 2)

    def test_inheritance(self):
        """Test if object is an instance of both classes"""
        obj = Rectangle(5, 3, 2, 1)
        self.assertIsInstance(obj, Rectangle)
        self.assertIsInstance(obj, Base)

    def test_invalid_width(self):
        """Test invalid width"""
        with self.assertRaises(ValueError):
            obj = Rectangle(-5, 3, 2, 1)

    def test_invalid_height(self):
        """Test invalid height"""
        with self.assertRaises(ValueError):
            obj = Rectangle(5, -3, 2, 1)

    def test_valid_x(self):
        """Test valid x"""
        try:
            obj = Rectangle(5, 3, 0, 1)
        except ValueError:
            self.fail("Exception was raised for valid x value")

    def test_valid_y(self):
        """Test valid y"""
        try:
            obj = Rectangle(5, 3, 2, 0)
        except ValueError:
            self.fail("Exception was raised for valid y value")

    def test_validate_attribute_inclusive(self):
        """Test validate_attribute method with inclusive flag set to True"""
        rect = Rectangle(5, 3, 2, 1)
        rect.validate_attribute("width", 5, inclusive=True)
        rect.validate_attribute("height", 3, inclusive=True)
        rect.validate_attribute("x", 2, inclusive=True)
        rect.validate_attribute("y", 1, inclusive=True)

    def test_validate_attribute_exclusive(self):
        """Test validate_attribute method with inclusive flag set to False"""
        rect = Rectangle(5, 3, 2, 1)
        with self.assertRaises(TypeError):
            rect.validate_attribute("width", "invalid", inclusive=False)
        with self.assertRaises(ValueError):
            rect.validate_attribute("width", 0, inclusive=False)
        with self.assertRaises(ValueError):
            rect.validate_attribute("height", 0, inclusive=False)
        with self.assertRaises(ValueError):
            rect.validate_attribute("x", 0, inclusive=False)
        with self.assertRaises(ValueError):
            rect.validate_attribute("y", 0, inclusive=False)


    def test_area(self):
        """Test the area method"""
        rect = Rectangle(5, 3, 2, 1)
        self.assertEqual(rect.area(), 15)

    def test_display(self):
        """Test the display method"""
        rect = Rectangle(5, 3, 2, 1)
        expected_output = "\n  #####\n  #####\n  #####\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            rect.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str(self):
        """Test the __str__ method"""
        rect = Rectangle(5, 3, 2, 1, 10)
        expected_output = "[Rectangle] (10) 2/1 - 5/3"
        self.assertEqual(str(rect), expected_output)

    def test_update(self):
        """Test the update method"""
        rect = Rectangle(5, 3, 2, 1, 10)
        rect.update(7, height=3, x=3)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 1)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        rect = Rectangle(5, 3, 2, 1)
        rect_dict = rect.to_dictionary()
        expected_dict = {"id": rect.id, "width": rect.width, "height": rect.height,
                        "x": rect.x, "y": rect.y}
        self.assertEqual(rect_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
