#!/usr/bin/python3
""" Module Square"""


class Square:
    """Square class defined by geometric shape

        Attributes:
            size(int): size of square

    """
    def __init__(self, size=0):
        """
        Initialize methode

        Args:
            size (int): size of square
        Raises:
            TypeError: if size is not int
            ValueError: if size is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
