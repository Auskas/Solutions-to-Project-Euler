# 
# Solution to Project Euler Problem 66 Diophantine equation.
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Euler
# The Brute force doesn't work. However, there are other algorithms to solve the so-called Pell's equation x**2 - D*y**2 = 1.
# This module uses the Chakravala method to find the solution.
# If the article on Wikipedia confuses you, there is another source that will give you more details:
# http://www.ms.uky.edu/~sohum/ma330/files/chakravala_alt.pdf

import time

def negative_modulus(x,y):
    """ Gets two integer numbers x and y.

    Returns the result of -x mod y. For instance, -10 mod 7 returns 4."""
    k = 1
    while x > k * y:
        k += 1
    return abs(x - k * y)
    

def chakravala(N):
    """ Gets the integer N of the Pell's equation.

    Returns the minimal solution of x using the Chakravala algorithm."""
    p = int(N ** (1/2))
    p0 = p
    q = 1
    m = p ** 2 - N
    x = negative_modulus(p, abs(m))
    # x must be lower than the square root of N, x + m must be bigger than the square root of N.
    while x + abs(m) <= p0:
        x += abs(m)
    #print(p,q,m)
    while m != 1:
        pprev = p
        p = int((pprev * x + N * q) / abs(m))
        q = int((pprev + x * q) / abs(m))
        m = (x ** 2 - N) / m
        x = negative_modulus(x, abs(m))
        while x + abs(m) <= p0:
            x += abs(m)
    return p

st_time = time.perf_counter()
# There are no other solutions than trivial when D is a square. Thus, we may skip it, that's why we precalculates the squares.
squares = {i ** 2 for i in range(2,32)}
max_x = 0
D = 0
for N in range(2,1001):
    if N in squares:
        continue
    x = chakravala(N)
    if x > max_x:
        max_x, D = x, N
print("The value of D = {0} gives the largest x = {1} in minimal solutions of quadratic Diophantine equations.".format(D, max_x))
print("The execution time is {0} seconds.".format(time.perf_counter() - st_time))

        
    


        
        
        
        
        
         
         
    
    

