#! /usr/bin/python3

# link to problem: https://projecteuler.net/problem=63

count = 1

for i in range(1,10):
    for j in range(1,25):
        a = i**j
        b = str(a)
        if len(b) == j:
            count += 1

print(count)
