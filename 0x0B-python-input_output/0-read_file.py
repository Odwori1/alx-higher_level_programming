#!/usr/bin/python3
"""Write module here"""


def read_file(filename=""):
    """func that reads a text file (UTF8) and prints
        Args:
        filename: filename
    """
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
        print(text, end="")
