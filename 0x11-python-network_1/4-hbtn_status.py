#!/usr/bin/python3
"""
python script that fetches a specific url
"""
import requests
html = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(html.text.__class__))
print("\t- content: {}".format(html.text))
