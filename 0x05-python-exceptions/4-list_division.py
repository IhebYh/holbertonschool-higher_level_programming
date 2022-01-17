#!/usr/bin/python3
"""
    prints list division

    """


def list_division(my_list_1, my_list_2, list_length):
    res = []
    for x in range(0, list_length):
        try:
            res.append(my_list_1[x] / my_list_2[x])
        except IndexError:
            print("out of range")
            res.append(0)
        except TypeError:
            print("wrong type")
            res.append(0)
        except ZeroDivisionError:
            print("division by 0")
            res.append(0)
        finally:
            pass
    return res
