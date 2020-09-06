#!/usr/bin/python3
def pow(a, b):
    power = 1
    if b == 0:
        return(power)
    elif b > 0:
        for i in range(b):
            power = power * a
        return(power)
    elif b < 0:
        for i in range(abs(b)):
            power = (1/a) * power
        return(power)
