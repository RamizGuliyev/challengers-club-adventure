#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.


def viralAdvertising(n):
    shared = 5
    liked = 2
    cumulative = 0
    for i in range(n):
        liked = shared//2
        cumulative = cumulative + liked
        shared = liked*3
    return cumulative


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
