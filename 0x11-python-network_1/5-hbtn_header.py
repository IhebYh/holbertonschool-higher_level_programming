#!/usr/bin/python3
"""
request module
"""
import requests
import sys

html = requests.get(sys.argv[1])
print(html.headers.get('X-Request-Id'))
