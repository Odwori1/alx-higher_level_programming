#!/usr/bin/python3
"""Write imported module here"""


def matrix_divided(matrix, div):
    """Function that divides matrix elements by div

    Args:
        matrix: two-dimensional matrix
        div: the divisor

    Raises:
        TypeError: if matrix does not contain elements of int or floats
        TypeError: if row of the matrix is not of the same size
        TypeError: if div is not float or integer
        ZeroDivisionError: if div is  0

    Returns:
        list of lists containing divided elements
    """

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists)" + " of integers/floats"
        )

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists)" + " of integers/floats"
            )
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists)" + " of integers/floats"
                )
    return [[round(element / div, 2) for element in row] for row in matrix]


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/2-matrix_divided.txt")
