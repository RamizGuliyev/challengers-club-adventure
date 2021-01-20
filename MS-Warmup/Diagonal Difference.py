#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    sum_pd = 0  # The primary diagonal
    sum_sd = 0  # The secondary diagonal

    # WAY 1
    # for element, i in zip(arr, range(len(arr))):
    #     sum_pd += element[i]
    #     sum_sd += element[len(arr)-1-i]
    # return(abs(sum_pd-sum_sd))

    # WAY 2
    # for i in range(len(arr)):
    #     sum_pd+=arr[i][i]
    #     sum_sd+=arr[i][len(arr)-1-i]
    # return(abs(sum_pd-sum_sd))

    # WAY 3
    ans = 0
    for i in range(len(arr)):
        ans += arr[i][i]
        ans -= arr[i][len(arr)-1-i]
    return(abs(ans))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
