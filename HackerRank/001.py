#!/bin/python3

def multiples(n, d):
    n//= d
    return d*n*(n+1) // 2

a, b = 3, 5

for _ in range(int(input())):
    m = int(input())-1
    total = multiples(m, a) + multiples(m, b) - multiples(m, a*b)
    print(total)
