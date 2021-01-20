#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.


def divisibleSumPairs(n, k, ar):
    ans = 0
    for i in range(len(ar)):
        for j in range(len(ar)):
            if i != j:
                if (ar[i]+ar[j]) % k == 0:
                    ans += 1
            else:
                continue
    pair = ans/2
    return int(pair)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
