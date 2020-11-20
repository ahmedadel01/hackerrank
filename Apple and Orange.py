"""
Link Problem -- >  https://www.hackerrank.com/challenges/apple-and-orange/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    number_apples = 0
    number_oranges = 0
    # count number of apples
    for apple in apples:
        x = a + apple
        if x >= s and x <= t:
            number_apples += 1
    # count number of orange
    for orange in oranges:
        y = b + orange
        if y >= s and y <= t:
            number_oranges += 1

    print(number_apples)
    print(number_oranges)

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
