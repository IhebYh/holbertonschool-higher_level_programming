#!/usr/bin/python3
"""
    prints x element of a list
"""


def safe_print_list(my_list=[], x=0):
    nb = 0
    for i in range(0, x):
        try:
            print("{:d}".format(i), end="")
            nb += 1
        except:
            break
    print("")
    return (nb)
