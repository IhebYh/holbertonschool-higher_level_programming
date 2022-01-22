#!/usr/bin/python3
"""
    Say my name module
"""


def say_my_name(first_name, last_name=""):
    """
        print the name
        Args:
            first_name(string): first name to print
            last_name(string): last name to print
        Raises:
            TypeError: both vars must be string
        Returns:
            None
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
