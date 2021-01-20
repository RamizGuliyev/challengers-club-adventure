#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0 
    negative = 0 
    zero = 0 
    for element in arr:
        if element>0:
            positive += 1
        elif element == 0:
            zero += 1
        else:
            negative +=1
    p_p_v = positive/len(arr)#proportion of positive values
    p_n_v = negative/len(arr)#proportion of negative values
    p_z = zero/len(arr)#proportion of zeros
    print(p_p_v)
    print(p_n_v)
    print(p_z)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)