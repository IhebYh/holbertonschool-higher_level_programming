#!/usr/bin/python3
"""
Student class module
"""


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

    def to_json(self, attrs=None):
        """
        retrieves a dict rep of a Student instance
        """
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {i: j for i, j in self.__dict__.items() if i in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
        replace all attributesof the Student instance
        """
        for i, j in json.items():
            self.__dict__[i] = j
