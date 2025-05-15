#! /usr/bin/python

# link to problem: https://projecteuler.net/problem=52

for i in range(1,1000000):
    a = str(i)
    b = str(2*i)
    c = str(3*i)
    d = str(4*i)
    e = str(5*i)
    f = str(6*i)

    new_set = {tuple(sorted(a))}

    if (
        len({len(a), len(b), len(c), len(d), len(e), len(f)}) == 1
        and {tuple(sorted(b)), tuple(sorted(c)), tuple(sorted(d)), tuple(sorted(e)), tuple(sorted(f))} == new_set
    ):
        print(int(a))       

