#!/usr/bin/python3
"""Write imported module here"""


def add_integer(a, b=98):
    """Function that adds 2 integers.

    Args:
        a: first integer
        b: second integer

    Raises:
        TypeError: if a or b is not float or an integer

    Returns:
        the sum of a and b
    """

    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest

    print(add_integer(4.45))
    doctest.testfile("tests/0-add_integer.txt")
