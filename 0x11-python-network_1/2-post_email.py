#!/usr/bin/python3
"""Sends an email"""

if __name__ == "__main__":
    """Sends data in a post request
    """
    import urllib.request
    import urllib.parse
    from sys import argv

    values = {'email': argv[2]}
    email = urllib.parse.urlencode(values)
    req = urllib.request.Request(argv[1], email)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('UTF-8'))
