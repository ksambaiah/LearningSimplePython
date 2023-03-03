#!/usr/bin/env pythn3


def gcd(a, b):
    if b == 0:
       return a
    return gcd(b, a mod b)

if __name__ == "main":
    print(gcd(20422, 24))

