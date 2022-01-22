#!/usr/bin/python3
"""
    print square module
"""


def print_square(size):
    """
    Print square with the character #
    Args:
        size(int): the size of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    Returns:
        None
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        print("#" * size)
