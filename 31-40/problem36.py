#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=36

def palindrome(num):
    new_num = num
    rem  = 0
    while(new_num>0):
            m = new_num%10
            rem = rem*10 + m
            new_num = new_num//10

    return num == rem

def binary(n):
    total = 0
    for i in range(1,n-1):
        bin_str = ''
        bin_num = ''
        if palindrome(i):
            a = i
            while a > 0:
                div = a%2
                a = a//2
                bin_str += str(div)
            
            for j in range(len(bin_str)):
                bin_num += bin_str[len(bin_str)-1-j]
            
            if palindrome(int(bin_num)):
                total += i

    return total
        
print(binary(10**6))
