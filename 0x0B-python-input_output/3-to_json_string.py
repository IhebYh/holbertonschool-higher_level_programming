#!/usr/bin/python3
"""
json to string module
"""


import json


def to_json_string(my_obj):
    """
    returns the JSON rep of an obj
    """
    return json.dumps(my_obj)
