#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.


def utopianTree(n):
    height = 1

    if n == 0:
        return height

    for i in range(2, n+2):
        if i % 2 == 0:
            height *= 2
        if i % 2 != 0:
            height += 1

    return height


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
