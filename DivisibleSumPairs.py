import math
import os
import random
import re
import sys


def divisibleSumPairs(n, k, ar):
    s = []
    for i in range(n):
        for j in range(i+1, n):
            if ((ar[i]+ar[j])%k) == 0:
                s.append((i, j))
    return len(list(set(s)))


nk = input().split()
n = int(nk[0])
k = int(nk[1])
ar = list(map(int, input().rstrip().split()))

result = divisibleSumPairs(n, k, ar)
print result
