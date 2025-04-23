#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=16

# defining function for finding the power digit sum
def power_and_sum(base, power):

    power_res = base ** power
    sum_res = sum(int (i) for i in str(power_res))

    return sum_res

print(power_and_sum(2, 1000))
