#!/usr/bin/python3
"""Fetching using requests library"""

if __name__ == "__main__":
    """Fetches a request using requests package
    """
    import requests

    r = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: ', type(r.text))
    print('\t- content: ', r.content.decode('UTF-8'))
