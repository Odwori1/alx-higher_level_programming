#!/usr/bin/python3
"""Write imported module here"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiply m_a by m_b using numpy matrices.

    Args:
        m_a: The first matrix.
        m_b: The second matrix.

    Returns:
        matrix: The product of m_a and m_b.

    Raises:
        TypeError:m_a or m_b is not a list , m list of lists, if elements are
               not int or float, or inner lists are not of the same len

        ValueError: if lists are empty, or items cannot be multiplied
        TypeError: If m_a or m_b have non-int/float values or are not rectangular.
    """

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a matrix (list of lists) of integers/floats")

    if len(m_a) == 0 or len(m_a[0]) == 0 or len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b cannot be multiplied")

    if any(not isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a must contain only integers/floats")

    if any(not isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b must contain only integers/floats")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise ValueError("m_a must be a rectangular matrix")

    if any(len(row) != len(m_b[0]) for row in m_b):
        raise ValueError("m_b must be a rectangular matrix")

    return numpy.matrix(m_a) * numpy.matrix(m_b)


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/101-lazy_matrix_mul.txt")
