#!/usr/bin/python3
import sys
"""
    fnc that prints an int
    """


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print('Exception: {}'.format(ex), file=sys.stderr)
        return False
