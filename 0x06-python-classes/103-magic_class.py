#!/usr/bin/python3

import math
"""
    Magic class module
"""


class MagicClass:
    def __init__(self, radius=0):
        """
        class init
        Args:
            radius (int): radius of a circle
        Raises:
            TypeError: if radius is not a number
        Returns:
            None
        """
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """
        area of a circle
        Returns:
            float
        """
        return self.radius ** 2 * math.pi

    def circumference(self):
        """
        circumference of a circle
        Returns:
            float
        """
        return 2 * math.pi * self.__radius
