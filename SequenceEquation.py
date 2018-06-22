#!/bin/python3


# Complete the permutationEquation function below.
def permutationEquation(p):
    r = []
    for i in range(1, len(p)+1):
        r.append((p[i-1], i))
    seq = sorted(r)
    e = []
    for i in range(1, len(seq)+1):
        index, val = seq[i-1]
        e.append(val)
    k = []
    for i in range(len(e)):
        k.append(e[e[i]-1])
    return k


if __name__ == '__main__':

    n = int(raw_input())

    p = list(map(int, raw_input().rstrip().split()))

    result = permutationEquation(p)

    print result
