#!/usr/bin/python3
"""Imported modules for the Base class"""
from json import dumps
from json import loads
import csv


class Base:
    """The Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to JSON string"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save objects to a file in JSON format"""
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        else:
            list_dicts = []

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string to a list of dictionaries"""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Loads an instance"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            new_instance = Rectangle(1, 1)
        elif cls is Square:
            new_instance = Square(1)
        else:
            new_instance = None

        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """A method that returns a list of instances"""

        from os import path

        file_name = "{}.json".format(cls.__name__)

        if not path.isfile(file_name):
            return []

        with open(file_name, "r", encoding="utf-8") as file:
            json_data = file.read()

        obj_dicts = cls.from_json_string(json_data)
        return [cls.create(**obj_dict) for obj_dict in obj_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method that makes object in csv file
        Args:
            list_objs: the list objects
        """
        if list_objs is not None:
            if cls.__name__ == 'Rectangle':
                list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                             for obj in list_objs]
            else:
                list_objs = [[obj.id, obj.size, obj.x, obj.y]
                             for obj in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Method that retrieves an object from the csv file"""
        load = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                row = [int(rw) for rw in row]
                if cls.__name__ == 'Rectangle':
                    attr = {"id": row[0], "width": row[1], "height": row[2],
                            "x": row[3], "y": row[4]}
                else:
                    attr = {"id": row[0], "size": row[1],
                            "x": row[2], "y": row[3]}
                load.append(cls.create(**attr))
        return load
