#!/usr/bin/python3
"""Imported module for add_item"""


def pascal_triangle(n):
    """Func that represents Pascal's triangle of n.

    Args:
        n: Number.

    Return:
        List of lists of integers.
    """
    triangle = []
    row = [1]
    temp = [0]
    for _ in range(max(n, 0)):
        triangle.append(row)
        row = [left + right for left, right in zip(row + temp, temp + row)]
    return triangle
