#! /usr/bin/python

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?

a = 2520

while True:
    if all(a % num == 0 for num in range(1,21)):
        break

    a = a+1

print(str(a) + " is the smallest number evenly divisible by all numbers from 1 to 20")
