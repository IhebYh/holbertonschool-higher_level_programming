#!/usr/bin/python3
"""
same class module
"""


def is_same_class(obj, a_class):
    """
    verify if the object is exactly an instance
    Args:
        obj(object): the object to verify
        a_class(class): the class to compare
    Returns:
        Either true or false
    """
    return (type(obj) is a_class)
