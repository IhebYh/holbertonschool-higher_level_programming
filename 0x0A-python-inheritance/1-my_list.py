#!/usr/bin/python3
"""
MyList module inherited from list
"""


class MyList(list):
    """
    MyList class
    """
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """
        print a sorted list
        """
        return (sorted(slef))
