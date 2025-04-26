#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=34

def fact_digit(n):
    factorial = 1
    for i in range(n):
        factorial *= (n-i)
    return factorial

num = 3 # since 1! and 2! are excluded
total = 0
while num < 1000000:
    fact = 0
    for i in range(len(str(num))):
        fact += fact_digit(int(str(num)[i]))
    if fact == num:
        total += fact
    num += 1

print(total)
