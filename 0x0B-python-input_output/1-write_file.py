#!/usr/bin/python3
"""Write module here"""


def write_file(filename="", text=""):
    """func that writes a string to a text file (UTF8)

    Args:
        filename: filename
        text: text to write

    Returns: the number of characters written
        """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
