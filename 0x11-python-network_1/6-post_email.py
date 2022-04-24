#!/usr/bin/python3
"""
requests model
"""

if __name__ == "__main__":
    import requests
    import sys
    d = {"email": sys.argv[2]}
    html = requests.post(sys.argv[1], data=d)
    print(html.text)
