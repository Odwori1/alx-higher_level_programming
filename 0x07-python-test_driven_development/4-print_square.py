#!/usr/bin/python3
"""Write imported module here"""


def print_square(size):
    """prints a square of #

    Args:
        size: the size in int of one side of the square
    Raises:
        TypeError: if size != int
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/4-print_square.txt")
