#!/usr/bin/python3
'''This modules requests'''
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
        print('Body response:$')
        print('\t- type: {}'.format(type(data)))
        print('\t- content: {}'.format(data))
