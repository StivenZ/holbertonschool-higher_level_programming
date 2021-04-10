#!/usr/bin/python3
"""Fetching header"""

if __name__ == "__main__":
    """Prints a variable value with requests package
    """
    import requests
    from sys import argv

    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
