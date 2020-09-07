#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    idx = 0

    if length - 1 == 0:
        print("0 arguments.")
    elif length - 1 == 1:
        print("{} argument:".format(len(sys.argv) - 1))
        print("{}: {}".format(length - 1, sys.argv[1]))
    elif len(sys.argv) - 1 > 1:
        print("{} arguments:".format(length - 1))
        for idx, val in enumerate(sys.argv[1:]):
            idx += 1
            print("{}: {}".format(idx, val))
