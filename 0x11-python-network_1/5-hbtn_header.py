#!/usr/bin/python3
"""
request module
"""
if __name__ == '__main__':
    import requests
    import sys
    html = requests.get(sys.argv[1])
    print(html.headers.get('X-Request-Id'))
