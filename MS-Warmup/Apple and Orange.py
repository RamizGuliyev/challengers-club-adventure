#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.


def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apples = 0
    count_oranges = 0
    for i in range(len(apples)):
        if s <= a+apples[i] <= t:
            count_apples += 1
        else:
            None
    for j in range(len(oranges)):
        if s <= b+oranges[j] <= t:
            count_oranges += 1
        else:
            None
    print(count_apples)
    print(count_oranges)  # Bu iki sətiri bir sətirdə yazmaq olardı


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
