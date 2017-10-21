#!/bin/python3

import sys

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
rodeo = 0


def simpleArraySum(n, ar):
    # Complete this function
    result = 0
    for r in ar:
        result += r
        print(result)


result = simpleArraySum(n, ar)
print(result)
print(n)


