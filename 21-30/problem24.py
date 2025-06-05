#! /usr/bin/python

# link to question: https://projecteuler.net/problem=24
import itertools

def perms(n):
    new_set = [i for i in range(n)]
    lexi_order = []
    
    for p in itertools.permutations(new_set):
        p_str = ''.join(str(x) for x in p)
        lexi_order.append(p_str)
        if len(lexi_order) == 10**6:
            break
    
    return lexi_order[10**6 - 1]

print(perms(10))
