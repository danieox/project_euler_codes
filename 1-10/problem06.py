#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=6

a = 0
b = 0

for i in range (1,101):
    a += i * i
    b += i

c = b * b
d = c - a

print("The sum of the squares of the first one hundred natural numbers is " + str(a))
print("\n The square of the sum of the first one hundred natural numbers is " + str (b))
print("\n Hence the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is " + str(d))
