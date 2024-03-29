#!/usr/bin/python3
"""
square class iherited from rectangle class module
"""
from ctypes import sizeof
from .rectangle import Rectangle


class Square(Rectangle):
    """
    square class representation
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ square init"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """ string rep"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width)

    def update(self, *args, **kwargs):
        """
        updates multiple attributes
        """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.size = j
                if i == 2:
                    self.x = j
                if i == 3:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
    def to_dictionary(self):
        """dictionnary representation of a square"""
        dict = {}
        dict["id"] = self.id
        dict["size"] = self.size
        dict["x"] = self.x
        dict["y"] = self.y
        return dict