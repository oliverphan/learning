#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    i = n
    step = " " * n
    while (i > 0):
        # step[i - 1] = "#" Doesn't work: Python strings are immutable so need to splice together new parts of array
        step = step[:i-1] + "#" + step[i:]
        print(step)
        i -= 1
        

if __name__ == '__main__':
    n = int(input())

    staircase(n)
