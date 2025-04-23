#! /usr/bin/python

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

max_palindrome = 0

for i in range(100,1000):
    for j in range(100,1000):
        a = i * j
        b = a
        rem = 0

        while(b>0):
            c = b%10
            rem = rem*10 + c
            b = b//10

        if a == rem and a > max_palindrome:
            max_palindrome = a
            p = i
            q = j

print(f"The largest palindrome made from the product of two 3-digit number: {p} and {q} is {max_palindrome}")
