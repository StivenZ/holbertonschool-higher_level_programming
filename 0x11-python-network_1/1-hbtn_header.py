#!/usr/bin/python3
"""Fetches variable's value in the header"""

if __name__ == "__main__":
    """Send a request and finds a variable.
    """
    import urllib.request
    from sys import argv

    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.headers['X-Request-Id'])
