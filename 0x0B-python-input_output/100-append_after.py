#!/usr/bin/python3
"""Imported module"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after a specific search string in a file.

    Args:
        filename (str): Name of the file.
        search_string (str): Text to search for.
        new_string (str): Text to insert after the search string.
    """
    lines = []
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    last_occurrence_index = None
    for idx, line in enumerate(lines):
        if search_string in line:
            last_occurrence_index = idx

    if last_occurrence_index is not None:
        lines.insert(last_occurrence_index + 1, new_string)

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)
