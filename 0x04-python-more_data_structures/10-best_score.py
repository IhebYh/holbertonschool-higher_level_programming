#!/usr/bin/python3
def best_score(a_dictionary):
    kv = 0
    k = ""
    for i in a_dictionary:
        if a_dictionary[i] > kv:
            k = i
            kv = a_dictionary[i]
    return k if k != "" else None
