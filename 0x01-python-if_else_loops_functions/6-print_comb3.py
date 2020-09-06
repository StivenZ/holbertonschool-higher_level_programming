#!/usr/bin/python3
for a in range(100):
    if a % 10 > a / 10:
        if a != 89:
            print("{:02d}".format(a), end=', ')
        else:
            print("{:02d}".format(a))
            