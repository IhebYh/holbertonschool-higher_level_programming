#!/usr/bin/python3
"""
my int module 
"""


class MyInt(int):
    """
        a rebel class that inherits  from int 
    """
    def __eq__(self, x):
        """equal"""
        return not super().__eq__(x)

    def __ne__(self, x):
        """ not equal"""
        return not super().__ne__(x)
