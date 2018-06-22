#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    s = 0
    if len(a) < k:
        return 'NO'
    else:
        for i in a:
            if int(i) <= 0:
                s = s + 1
        if s >= k:
            return 'NO'
        else:
            return 'YES'


if __name__ == '__main__':
    result = []
    t = int(str(raw_input()))

    for t_itr in range(t):
        nk = str(raw_input()).split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, str(raw_input()).rstrip().split()))

        result.append(angryProfessor(k, a))
    print (result)


