#!/usr/bin/python3
""" Module Square"""


class Square:
    """Square class defined by geometric shape

        Attributes:
            size(int): size of square
            position (tuple): the square position
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize methode

        Args:
            size (int): size of square
            position (tuple): position of square in 2D space
        Returns:
            None
        """
        self.__size = size
        self.position = position

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

    def my_print(self):
        """
            print the square from the size using #

            Return:
                None
        """
        if self.__size > 0:
            print('\n' * self.__position[1], end="")
            for i in range(self.size):
                print(" " * self.__position[0], end="")
                print("#" * self.size)
        else:
            print()

    @property
    def position(self):
        """
            get the square position

            Return:
                the current square pos
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            set the square position

            Args:
                position (tuple): position of a side of the square
            Return:
                None
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        string = ""
        if self.__size == 0:
            return "\n"

        string += '\n'*self.__position[1]
        for i in range(self.__size):
            string += ' '*self.__position[0]
            string += '#'*self.__size
            if i is not self.__size - 1:
                string += '\n'
        return string
