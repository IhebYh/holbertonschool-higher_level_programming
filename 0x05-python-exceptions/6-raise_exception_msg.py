#!/usr/bin/python3
"""
    raise exception message

    """


def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except:
        raise
