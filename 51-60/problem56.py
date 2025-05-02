#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=56

max_sum = 0
for a in range(1,100):
    for b in range(1,100):
        c = a**b
        d = str(c)
        temp  = 0
        for i in range(len(d)):
            temp += int(d[i])
            if temp > max_sum:
                max_sum = temp

print(max_sum)
