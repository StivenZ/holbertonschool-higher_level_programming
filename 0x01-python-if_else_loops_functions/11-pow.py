#!/usr/bin/python3
def pow(a, b):
    power = 1
    i = 0
    if b == 0:
        return(power)
    elif b > 0:
        while i < b:
            power = power * a
            i += 1
        return(power)
    elif b < 0:
        while i < abs(b):
            power = (1/a) * power
            i += 1
        return(power)
