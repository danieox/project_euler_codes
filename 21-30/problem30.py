#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=30
digit_fifth_pow =[]
n = (9**5)*9
for a in range(2,n):
    b = str(a)
    c = 0
    for i in range(len(b)):
        c += int(b[i])**5
    if a == c:
        digit_fifth_pow.append(a)

print(sum(digit_fifth_pow))
