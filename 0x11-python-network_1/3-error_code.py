#!/usr/bin/python3
"""
HTTP ERROR HANDLING
"""
from sys import argv
from urllib import request, error

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as res:
            info = res.read()
            print(info.decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
