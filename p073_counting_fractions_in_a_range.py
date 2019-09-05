# 
# Solution to Project Euler Problem 73 Counting fractions in a range.
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Euler
# There are the formulae to calculate the numerator and denominator of the next fraction in the Farey sequence.
# All we need to know is two neighboring fractions in the sequence. The first step is to get the next fraction to the right of 1/3.
# The last step is straighforward: we generate next fractions counting terms until the fraction is 1/2.


import time

def neighbor(a=1,b=3,n=12000):
    """ Gets the numerator a and the denominator b of one of the fractions as well as the order of the Farey sequence.

    Returns the next fraction to the right in the sequence."""
    # It is known that the difference between two neighboring fractions can be found from the equation c/d - a/b = 1/bd, where c/d > a/b are neighbors.
    # Thus, bc - ad = 1. Browsing through various values of d in the range from n=12000 to 2, we need to find a proper c so that c = (d + 1) / 3 is an integer.
    # Spoiler: d = 11999, c = 4000.
    for d in range(n,1,-1):
        if (d + 1) % 3 == 0:
            c = (d + 1) // 3
            break
    return c, d

def range_counting(a,b,c,d,n=12000,terms=1):
    """ Gets the values of numerator and denominator of two fractions a/b,c/d. Generates next fractions in the Farey sequence counting terms.

    Return the number of terms when the next fraction is 1/2."""    
    while True:
        p = ((n + b) // d) * c - a
        q = ((n + b) // d) * d - b
        if p == 1 and q == 2:
            return terms
        terms += 1
        a, b, c, d = c, d, p, q

st_time = time.perf_counter()
c, d = neighbor(1, 3)
print("The number of fractions between 1/3 and 1/2 in the Farey sequence when the denominator <= 12000 equals to {0}".format(range_counting(1,3,c,d)))
print("The execution time is {0} seconds.".format(time.perf_counter() - st_time))



    


