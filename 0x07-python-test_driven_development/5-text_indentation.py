#!/usr/bin/python3
"""Write imported module here"""


def text_indentation(text):
    """Func that adds new lines when it finds these char in string: ., :, ?

    Args:
        text: the string to print

    Raises:
        TypeError: if the text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        nline = char + "\n\n"
        text = nline.join([line.strip(" ") for line in text.split(char)])
    print(text, end="")


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/5-text_indentation.txt")
