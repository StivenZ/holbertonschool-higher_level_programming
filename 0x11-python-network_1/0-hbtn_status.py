#!/usr/bin/python3
"""Module on fetching with urllib library"""

if __name__ == "__main__":
    """Fetch an url with format
    """
    import urllib.request

    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        the_page = the_page.decode('UTF-8')
        print('Body response:')
        for id in the_page:
            print('\t- {}: {}'.format(id, type(id)))
