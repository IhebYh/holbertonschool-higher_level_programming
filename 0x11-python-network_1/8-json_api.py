#!/usr/bin/python3
"""
Search API
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    try:
        arg = argv[1]
    except Exception:
        arg = ""
    d = {"q": arg}
    r = requests.post("http://0.0.0.0:5000/search_user", data=d)
    try:
        res = r.json()
    except Exception:
        print("Not a valid JSON")
        exit()
    try:
        print("[{}] {}".format(res['id'], res['name']))
    except Exception:
        print("No result")
