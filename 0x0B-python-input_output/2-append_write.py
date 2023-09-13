#!/usr/bin/python3
"""Write module here"""


def append_write(filename="", text=""):
    """func that appends a string to a text file (UTF8)

    Args:
        filename: filename
        text: text to append

    Returns: the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
