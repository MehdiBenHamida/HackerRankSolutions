#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the formingMagicSquare function below.

def cal_cost(lst1, lst2):
    cost = 0
    for i in range(len(lst1)):
        cost = cost + abs(lst1[i]-lst2[i])
    return cost

def formingMagicSquare(s):
    matrix_list = [[8, 1, 6, 3, 5, 7, 4, 9, 2],
                   [6, 1, 8, 7, 5, 3, 2, 9, 4],
                   [4, 9, 2, 3, 5, 7, 8, 1, 6],
                   [2, 9, 4, 7, 5, 3, 6, 1, 8],
                   [8, 3, 4, 1, 5, 9, 6, 7, 2],
                   [4, 3, 8, 9, 5, 1, 2, 7, 6],
                   [6, 7, 2, 1, 5, 9, 8, 3, 4],
                   [2, 7, 6, 9, 5, 1, 4, 3, 8]]
    costs = []
    for mat in matrix_list:
        costs.append(cal_cost(s, mat))
    return min(costs)


if __name__ == '__main__':
    s = []

    for _ in range(3):
        s.append(list(map(int, str(raw_input()).rstrip().split())))
    r = []
    for l in s:
        for el in l:
            r.append(el)
    result = formingMagicSquare(r)

    print result
