#!/usr/bin/python3
"""
Post an email to an url
"""
from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    value = {"email": argv[2]}
    data = parse.urlencode(value)
    data = data.encode("ascii")
    req = request.Request(argv[1], data)
    with request.urlopen(req) as res:
        info = res.read()
    print(info.decode("ascii"))
