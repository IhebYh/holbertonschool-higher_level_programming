#!/usr/bin/python3
"""
Student to JSON module
"""


from re import A


class Student:
    """
    class that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        init
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dict rep of a Student instance
        """
        return self.__dict__
