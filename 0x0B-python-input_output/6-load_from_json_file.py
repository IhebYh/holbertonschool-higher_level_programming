#!/usr/bin/python3
"""
load from json file module
"""


import json


def load_from_json_file(filename):
    """
    creates an object from "JSON file"
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
