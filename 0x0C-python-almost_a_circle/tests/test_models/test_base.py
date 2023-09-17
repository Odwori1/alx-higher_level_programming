#!/usr/bin/python3
"""Imported modules for the Base test class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import os
from models.square import Square

class TestBase(unittest.TestCase):
    """Class to write test cases for the base class"""

    def setUp(self):
        """Method called before each test method"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """Method called after each test method"""
        pass

    def test_constructor_with_id(self):
        """Test constructor with id variable"""
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_constructor_without_id(self):
        """Test constructor without id"""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_private_class_variable_exists(self):
        """Test if __nb_objects exists"""
        base_instance = Base()
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_private_class_variable_initial_value(self):
        """Test if __nb_objects has an initial value of 0"""
        base_instance = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 1)
        self.assertEqual(base_instance._Base__nb_objects, 1)

    def test_to_json_string(self):
        """Test for to_json_string method with empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")

        """Test with list of dictionaries"""
        data = [
            {"id": 1, "name": "Marsiya"},
            {"id": 2, "name": "Issah"}
        ]
        expected_output = '[{"id": 1, "name": "Marsiya"}, {"id": 2, "name": "Issah"}]'
        self.assertEqual(Base.to_json_string(data), expected_output)

        """ Test with None"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string(self):
        """Test for from_json_string method with empty string"""
        self.assertEqual(Base.from_json_string(""), [])

        """Test with JSON string"""
        json_string = '[{"id": 1, "name": "Marsiya"}, {"id": 2, "name": "Issah"}]'
        expected_output = [
            {"id": 1, "name": "Marsiya"},
            {"id": 2, "name": "Issah"}
        ]
        self.assertEqual(Base.from_json_string(json_string), expected_output)

        """ Test with None"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_save_to_file(self):
        """ Create a list of Rectangle objects"""
        rectangles = [
            Rectangle(4, 6, 2, 3),
            Rectangle(5, 3, 1, 2)
        ]

        Rectangle.save_to_file(rectangles)

        filename = Rectangle.__name__ + ".json"
        with open(filename, "r") as file:
            content = file.read()

        self.assertTrue(content.startswith("["))
        self.assertTrue(content.endswith("]"))

        json_data = Rectangle.from_json_string(content)

        self.assertEqual(len(rectangles), len(json_data))

        for orig_rect, saved_rect_dict in zip(rectangles, json_data):
            self.assertEqual(orig_rect.to_dictionary(), saved_rect_dict)

        os.remove(filename)

        rectangles = [
                Rectangle(4, 6, 2, 3),
                Rectangle(5, 3, 1, 2)
            ]

        """Save and read the rectangles to a file"""
        Rectangle.save_to_file(rectangles)

        filename = Rectangle.__name__ + ".json"
        with open(filename, "r") as file:
            content = file.read()


        self.assertTrue(content.startswith("["))
        self.assertTrue(content.endswith("]"))


        json_data = Rectangle.from_json_string(content)

        self.assertEqual(len(rectangles), len(json_data))

        for orig_rect, saved_rect_dict in zip(rectangles, json_data):
            self.assertEqual(orig_rect.width, saved_rect_dict["width"])
            self.assertEqual(orig_rect.height, saved_rect_dict["height"])
            self.assertEqual(orig_rect.x, saved_rect_dict["x"])
            self.assertEqual(orig_rect.y, saved_rect_dict["y"])
            self.assertEqual(orig_rect.id, saved_rect_dict["id"])

        os.remove(filename)

    def test_create_rectangle(self):
        """ Create a dictionary with values for a Rectangle"""
        rect_dict = {"id": 1, "width": 5, "height": 3, "x": 2, "y": 1}


        rect = Rectangle.create(**rect_dict)
        self.assertIsInstance(rect, Rectangle)

        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 1)

    def test_create_square(self):
        """ Create a dictionary with values for a Square"""
        square_dict = {"id": 20, "size": 4, "x": 9, "y": 22}

        square = Square.create(**square_dict)

        self.assertIsInstance(square, Square)

        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 9)
        self.assertEqual(square.y, 22)

    def test_load_from_file_rectangle(self):
        """Test load_from_file method from rect"""
        rectangles = [Rectangle(2, 3), Rectangle(4, 5)]
        Rectangle.save_to_file(rectangles)

        loaded_rectangles = Rectangle.load_from_file()

        self.assertEqual(len(loaded_rectangles), 2)
        self.assertIsInstance(loaded_rectangles[0], Rectangle)
        self.assertIsInstance(loaded_rectangles[1], Rectangle)
        self.assertEqual(loaded_rectangles[0].width, 2)
        self.assertEqual(loaded_rectangles[0].height, 3)
        self.assertEqual(loaded_rectangles[1].width, 4)
        self.assertEqual(loaded_rectangles[1].height, 5)

    def test_load_from_file_square(self):
        """Test load_from_file method from square"""
        squares = [Square(2), Square(4)]
        Square.save_to_file(squares)

        loaded_squares = Square.load_from_file()

        self.assertEqual(len(loaded_squares), 2)
        self.assertIsInstance(loaded_squares[0], Square)
        self.assertIsInstance(loaded_squares[1], Square)
        self.assertEqual(loaded_squares[0].size, 2)
        self.assertEqual(loaded_squares[1].size, 4)

    def test_load_from_file_empty(self):
        """"Test load_from_file method from empty file"""
        file_name = "{}.json".format(Rectangle.__name__)
        with open(file_name, "w") as f:
            f.write("[]")

        loaded_objects = Rectangle.load_from_file()

        self.assertEqual(len(loaded_objects), 0)


    def test_save_to_file_csv_rectangle(self):
        """Test method  Create some Rectangle objects"""
        r1 = Rectangle(5, 3, 2, 1)
        r2 = Rectangle(7, 4, 3, 2)
        r3 = Rectangle(2, 2, 1, 1)
        rectangles = [r1, r2, r3]

        Rectangle.save_to_file_csv(rectangles)

        with open('Rectangle.csv', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        expected_lines = ['1,5,3,2,1\n', '2,7,4,3,2\n', '3,2,2,1,1\n']
        self.assertEqual(lines, expected_lines)

    def test_save_to_file_csv_square(self):
        """Test Create some Square objects"""
        s1 = Square(5, 2, 3)
        s2 = Square(7, 1, 1)
        s3 = Square(3, 0, 0)
        squares = [s1, s2, s3]

        Square.save_to_file_csv(squares)

        with open('Square.csv', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        expected_lines = ['1,5,2,3\n', '2,7,1,1\n', '3,3,0,0\n']
        self.assertEqual(lines, expected_lines)

    def test_load_from_file_csv_rectangle(self):
        """Test Load Rectangle objects from CSV file"""
        rectangles = Rectangle.load_from_file_csv()

        self.assertEqual(len(rectangles), 3)

        self.assertEqual(rectangles[0].width, 5)
        self.assertEqual(rectangles[0].height, 3)
        self.assertEqual(rectangles[0].x, 2)
        self.assertEqual(rectangles[0].y, 1)

        self.assertEqual(rectangles[1].width, 7)
        self.assertEqual(rectangles[1].height, 4)
        self.assertEqual(rectangles[1].x, 3)
        self.assertEqual(rectangles[1].y, 2)

        self.assertEqual(rectangles[2].width, 2)
        self.assertEqual(rectangles[2].height, 2)
        self.assertEqual(rectangles[2].x, 1)
        self.assertEqual(rectangles[2].y, 1)

    def test_load_from_file_csv_square(self):
        """Test Load Square objects from CSV file"""
        squares = Square.load_from_file_csv()

        self.assertEqual(len(squares), 3)

        self.assertEqual(squares[0].size, 5)
        self.assertEqual(squares[0].x, 2)


if __name__ == '__main__':
    unittest.main()
