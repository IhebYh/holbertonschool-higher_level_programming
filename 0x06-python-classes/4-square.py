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

        Returns:
            None
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
            set square area

            Return:
                the current square area (int)
        """
        return self.__size ** 2

    @property
    def size(self):
        """
            get the square size

            Return:
                the current square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            set the square size

            Args:
                size (int): size of a side of the square
            Raises:
                TypeError: if size is not int
                ValueError: if size is less than 0
            Return:
                None
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
