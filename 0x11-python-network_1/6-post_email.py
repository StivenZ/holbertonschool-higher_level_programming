#!/usr/bin/python3
"""Fetching header"""

if __name__ == "__main__":
    """Prints a variable value with requests package
    """
    import requests
    from sys import argv

    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.content.decode('UTF-8'))
