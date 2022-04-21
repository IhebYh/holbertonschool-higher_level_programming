#!/usr/bin/python3
def find_peak(a):
    """
    find peak module
    """
    if a == []:
        return None
    if len(a) == 1:
        return a[0]
    if a[0] >= a[1]:
        return a[0]
    if a[len(a) - 1] >= a[len(a) - 2]:
        return a[len(a) - 1]
    for i in range(1, len(a) - 1):
        if a[i] >= a[i - 1] and a[i] >= a[i + 1]:
            return a[i]
