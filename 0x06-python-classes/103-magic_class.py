#!/usr/bin/python3

import math
"""
    Magic class module
"""


class MagicClass:
    def __init__(self, radius=0):
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.radius = None

    def area(self):
        return self.radius ** 2 * math.pi

    def circumference(self):

        return 2 * math.pi * self.__radius
