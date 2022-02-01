#!/usr/bin/python3
"""
returns an object (PDS) represented by JSON string
"""


import json


def to_json_string(my_obj):
    """
    returns an object (PDS) represented by JSON string
    """
    return json.loads(my_obj)
