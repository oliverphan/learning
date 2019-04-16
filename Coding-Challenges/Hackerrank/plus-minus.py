#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    size = len(arr)
    count = {"pos": 0, "neg": 0, "zero": 0}
    for i in range(0, size):
        if arr[i] > 0:
            count["pos"] +=1 
        elif arr[i] == 0:
            count["zero"] += 1
        else:
            count["neg"] += 1
    
    print(count["pos"]/size)
    print(count["neg"]/size)
    print(count["zero"]/size)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
