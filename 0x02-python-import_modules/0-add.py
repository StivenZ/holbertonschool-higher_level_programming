#!/usr/bin/python3
import add_0 as ad
if __name__ == "__main__":
    ad.a = 1
    ad.b = 2
    print("{} + {} = {}".format(ad.a, ad.b, ad.add(1, 2)))
