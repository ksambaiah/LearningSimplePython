#!/usr/bin/env pythn3


def gcd(a, b):
    if b == 0:
       return a
    return gcd(b, a % b)

if __name__ == "__main__":
    print(gcd(20422, 42))

