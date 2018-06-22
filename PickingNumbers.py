#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pickingNumbers function below.
def pickingNumbers(a):
    k = []
    for i in range(len(a)):
        k.append(a.count(a[i]) + a.count(a[i] + 1))
        k.append(a.count(a[i]) + a.count(a[i] - 1))
    return max(k)


if __name__ == '__main__':
    n = int(raw_input())
    a = list(map(int, raw_input().rstrip().split()))
    result = pickingNumbers(a)
    print result
