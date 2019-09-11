# 
# Solution to Project Euler Problem 100 Arranged probability.
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Euler
# Gosh! Spent several hours trying to find a proper algorithm. Nevertheless, it is beneath one's nose.
# The very first thing to realize is the fact that the fraction "blue_disks / total_disks" tends to the square root of 1/2.
# Indeed, the bigger x and y in the equation x/y * (x-1)/(y-1) = 1/2, the closer x/y to the square root of 1/2.
# All we need to do is to generate the convergents of square root of 1/2.
# Next we need to form a non-reduced fraction out of the convergents so that x/y * (x-1)/(y-1) = 1/2.
# Once y > 10 ** 12 we're done.

import time

def fraction_form(p,q):
    """ Gets a proper reduced fraction p/q.

    Returns a non-reduced fraction that satisfies the condition of the problem (for any number of disks)."""
    # The fraction close to the square root of 1/2.
    # If p/q is bigger than the square root, returns a non-reduced fraction so that (p*x)/(q*x) * (p*x-1)/(q*x-1) = 1/2.
    # The root of the equation 2*p - q.
    # If p/q is less than the square root, returns a non-reduced fraction so that ((p*x)/(q*x) * (p*x+1)/(q*x+1) = 1/2.
    # The root is the same, however, it is the fraction to the right in x/y * (x-1)/(y-1). That is why we add additional 1 for p and q.
    square_root = (1/2) ** (1/2)
    if p/q > square_root:
        return p * (2 * p - q), q * (2 * p - q)
    return p * (2 * p - q) + 1, q * (2 * p - q) + 1
        
def fractions(a=0,x=(1/2)**(1/2),p_prev2=1,q_prev2=0,p_prev1=0,q_prev1=1):
    """ Gets coefficients to form the convergents of the square root of 1/2.
    After each iteration calls the function fraction_form(p,q) to get a non-reduced fraction.
    Returns the non-reduced fraction once the denominator is bigger than 10 ** 12."""
    # Simply google the article Continued fraction on Wikipedia if you don't get it.    
    a = int(1 / x)
    x = (1 / x) - a
    p = a * p_prev1 + p_prev2
    q = a * q_prev1 + q_prev2
    blue, total = fraction_form(p,q)
    if total > 10 ** 12:
        return blue, total
    p_prev2, q_prev2 = p_prev1, q_prev1
    p_prev1, q_prev1 = p, q
    return fractions(a,x,p_prev2,q_prev2,p_prev1,q_prev1)


st_time = time.perf_counter()
blue, total = fractions()
print("There is the probability of 1/2 of taking two blue disks in a row when the total number of the disks {0} and the number of blue disks {1}".format(total,blue))
print("The execution time is {0} seconds.".format(time.perf_counter() - st_time))
