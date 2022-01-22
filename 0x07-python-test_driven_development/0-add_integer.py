#!/usr/bin/python3

"""
Add int of float module
"""


def add_integer(a, b=98):
    """
    a function to add integers
    Args:
        a(int/float): first int
        b(int/float): second int
    Raises:
        TypeError: when a or b is not an int or a float
    Return:
        integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if (a + b) == float('inf') or (a + b) == -float('inf'):
            return b
    return int(a) + int(b)
