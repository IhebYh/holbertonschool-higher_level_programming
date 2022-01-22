#!/usr/bin/python3
"""
 Text indentation module
"""


def text_indentation(text):
    """
    prints two lines after each of these characters: ., ?, :
    Args:
        text(string): the text to indent
    Raises:
        TypeError: if text is not string
    Returns:
        None
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    l = 0
    while l < len(text):
        if text[l] in [':', '.', '?']:
            print(text[l])
            print()
            l += 1
        else:
            print(text[l], end='')
        l += 1
