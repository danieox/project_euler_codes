#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=33
import math
from fractions import Fraction

curious_fractions = []
for a in range(10,100):
    for b in range(10,100):
        if a % 10 == 0 and b % 10 == 0:
            continue
        c = a/b
        m = str(a)
        n = str(b)
        common = set(m) & set(n)
        if common:
            for ch in common:
                m_new = m.replace(ch, '', 1)
                n_new = n.replace(ch, '', 1)
                if m_new and n_new != '0' and c == int(m_new)/int(n_new) and c < 1:
                    curious_fractions.append ((a,b,c))

frac = [x[2] for x in curious_fractions]
temp = 1
for i in range(len(frac)):
    temp *= Fraction(frac[i]).limit_denominator()

denom = temp.denominator
print(denom)

