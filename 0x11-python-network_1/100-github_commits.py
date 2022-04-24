#!/usr/bin/python3
"""
github repo fetching
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    res = requests.get(url)
    r = res.json()[:10]
    for i in r:
        key = i['sha']
        a = i['commit']['author']['name']
        print('{}: {}'.format(key, a))
