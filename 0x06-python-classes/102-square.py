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

    def __eq__(self, other):
        """
        check if square is equal to other square
        """
        return self.size == other.size

    def __ne__(self, other):
        """
        check if square is not equal to other square
        """
        return self.size != other.size

    def __gt__(self, other):
        """
        check if square is greater than other square
        """
        return self.size > other.size

    def __lt__(self, other):
        """
        check if square is less than other square
        """
        return self.size < other.size

    def __ge__(self, other):
        """
        check if square is greater than or equal to other square
        """
        return self.size >= other.size

    def __le__(self, other):
        """
        check if square is less than or equal to other square
        """
        return self.size <= other.size
