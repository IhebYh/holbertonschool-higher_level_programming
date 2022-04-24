#!/usr/bin/python3
"""
request module
"""
import requests
from sys import argv

html = requests.get(argv[1])
print(html.headers.get('X-Request-Id'))
