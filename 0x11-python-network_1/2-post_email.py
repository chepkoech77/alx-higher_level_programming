#!/usr/bin/python3
'''This module sends POST request'''
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        res = response.read().decode('utf-8')
        print(res)
