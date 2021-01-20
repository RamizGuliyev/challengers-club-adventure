#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.


def breakingRecords(scores):
    lowest = 0
    highest = 0
    sample = scores[0]
    for element in scores:
        if sample > element:
            highest += 1
            sample = element
    sample = scores[0]
    for element in scores:
        if sample < element:
            lowest += 1
            sample = element

    return lowest, highest


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
