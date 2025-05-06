#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    f = [1,2]

    while(f[-1] + f[-2]) <= n:
        f.append(f[-1] + f[-2])

    g = [i for i in f if i%2 == 0]
    print(sum(g))
