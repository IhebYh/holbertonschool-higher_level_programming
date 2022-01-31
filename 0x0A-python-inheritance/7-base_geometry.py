#!/usr/bin/python3
"""
base geometry module
"""


class BaseGeometry():
    """
    base geomtry class
    """
    def area(self):
        """
        public instance
        Raises:
            exception: area not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer validator
        Args:
            name(string): name
            value(int): vlaue to validate
        Raises:
            TypeError:if value is not an int
            ValueError: if value is less or equal to 0
        Returns:
            void
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
