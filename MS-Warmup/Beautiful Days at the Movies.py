#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.


def beautifulDays(i, j, k):
    # WAY 1
    count = 0
    for l in range(i, j+1):
        n = (str(l)[::-1])  # 'int' object is not subscriptable
        if(abs(l-int(n)) % k == 0):
            count += 1
    return count

    # WAY 2 ( Need modification)
    # rev = 0
    # count = 0
    # for n in range(i,j+1):
    #     while(n > 0):
    #         a = n % 10
    #         rev = rev * 10 + a
    #         n = n // 10
    #     if abs(n-rev)%k==0:
    #         print(abs(n-rev))
    #         count+=1

    # return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
