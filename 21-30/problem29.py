#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=29

Power_set = []

for a in range(2,101):
    for b in range(2,101):
        if a**b not in Power_set:
            Power_set.append(a**b)

print(len(Power_set))
