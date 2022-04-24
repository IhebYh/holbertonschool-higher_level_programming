#!/usr/bin/python3
"""
GitHub credentials uses
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    info = (argv[1], argv[2])  # (username, password)
    res = requests.get('https://api.github.com/user', auth=info)
    try:
        print(res.json()['id'])
    except Exception:
        print('None')
