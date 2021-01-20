#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.


def migratoryBirds(arr):
    # 5 types of birds (6 dənə sıfır çünki i~ın qiymətləri 1~5 arası dəyişir)
    typesss = [0, 0, 0, 0, 0, 0]
    for i in arr:
        typesss[i] += 1
    # Burda lower index de olanı seçməli olduğunu hardan bildi?
    return typesss.index(max(typesss))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
