#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=9

for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c = 1000 - a - b
        if c > b and (a * a + b * b == c * c):
            prod = a * b * c
            print(f"a = {a}, b = {b}, c = {c}")
            print(f"Product: {prod}")
            break
