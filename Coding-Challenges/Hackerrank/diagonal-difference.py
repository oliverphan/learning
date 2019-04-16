"""SETUP THE QUESTION FIRST"""
# First we have the side length of the matrix. store that in a variable, and it will be used in our loop condition

# We need two variables to keep track of a runnign total for each diagonal.

# the left to bottom diagonal will have both starting at 0,0 indices and increment by 1 each loop

# the right to bottom left diagonal will start at 0, (side length) and the column will increament by 1, while row decreases by 1

# Then return the absolute value difference

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    side_length = len(arr)
    row = 0
    col = 0

    # Top left to bottom right
    sum1 = 0
    while (row < side_length) and (col < side_length):
        sum1 += arr[row][col]
        row += 1
        col += 1

    # Top right to bottom left
    row = 0
    col = side_length - 1
    sum2 = 0
    while (row < side_length) and (col >= 0):
        sum2 += arr[row][col]
        row += 1
        col -= 1

    return abs(sum1 - sum2)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
