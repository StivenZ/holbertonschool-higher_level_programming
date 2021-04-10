#!/usr/bin/python3
"""Fetching header"""

if __name__ == "__main__":
    """Prints a variable value with requests package
    """
    import requests
    from sys import argv

    r = requests.get(argv[1])
    s_code = r.status_code

    if s_code >= 400:
        print('Error code:', s_code)
    else:
        print(r.content.decode('UTF-8'))
