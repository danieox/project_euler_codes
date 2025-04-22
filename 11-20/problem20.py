#! /usr/bin/python

# n! means n x (n-1) x ... x 3 x 2 x 1
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!. 

# function for finding factorials
def fact_digit(n):
    factorial = 1
    for i in range(n):
        factorial *= (n-i)
    return factorial

a = fact_digit(100)
b = str(a)
sum_digit = 0

for i in b:
    sum_digit += int(i)

print("Sum of the factorial is ", sum_digit)
