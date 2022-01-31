#!/usr/bin/python3
"""
Square module
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square class inherited from rect class
    """
    def __init__(self, size):
        """
            class init
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        string rep of the square
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
