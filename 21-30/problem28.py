#! /usr/bin/python

# link to problems: https://projecteuler.net/problem=28

def spiral(num):
    A = [1]
    a = 1
    limit = 2
    count = 0

    while a < num:
        a += limit
        A.append(a)
        count += 1

        if count == 4:
            count = 0
            limit += 2

    return sum(A)

# 1001 x 1001 = 1002001
print(spiral(1002001))
