#!/usr/bin/python3
"""
prints safe ints

"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except:
        return(False)
