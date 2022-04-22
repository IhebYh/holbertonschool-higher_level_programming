#!/usr/bin/python3
"""
python script that fetches a specific url
"""
from urllib import request


with request.urlopen('https://intranet.hbtn.io/status') as res:
    html = res.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(html), html, html.decode('utf-8')))
