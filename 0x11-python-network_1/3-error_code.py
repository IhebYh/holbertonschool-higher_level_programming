#!/usr/bin/python3
"""
HTTP ERROR HANDLING
"""
from sys import argv
from urllib import request, parse, error

if __name__ == "__main__":
    value = {"email": argv[2]}
    data = parse.urlencode(value)
    data = data.encode("ascii")
    req = request.Request(argv[1], data)
    try:
        with request.urlopen(req) as res:
            info = res.read()
            print(info.decode("ascii"))
    except error.HTTPError as e:
        print("Error code {}".format(e.code))
