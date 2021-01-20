#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    stock = []
    ans = 0

    for i in range(len(ar)):
        if ar[i] not in ar[0:i] and ar[i:]:
            stock.append(ar.count(ar[i]))
    for j in range(len(stock)):
        ans += stock[j]//2

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
