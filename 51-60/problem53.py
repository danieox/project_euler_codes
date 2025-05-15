#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=53

def fact(num):
    factorial = 1
    for i in range(num):
        factorial *= (num-i)
    return factorial

def combinatorics(n,r):
    total_combinations = fact(n)/(fact(r)*fact(n-r))
    return total_combinations

count = 0
for n in range(1,101):
    for r in range(n):
        a = combinatorics(n,r)
        if a > 10**6:
           count += 1
           
print(count)

