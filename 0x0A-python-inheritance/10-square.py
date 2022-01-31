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
        self.__size = size
        self.integer_validator('size', self.__size)

    def area(self):
        """
        area of the square
        """
        return self.__size ** 2

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
