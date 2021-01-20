#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.


def bonAppetit(bill, k, b):
    # First case
    actual = (sum(bill) - bill[k])/2
    # Second Case
    if b-actual == 0:
        print("Bon Appetit")
    else:
        print(int(b-actual))


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
