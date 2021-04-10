#!/usr/bin/python3
"""Manages Error"""

if __name__ == "__main__":
    """Sends request and manages HTTPError.
    """
    import urllib
    import urllib.request
    from sys import argv

    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
