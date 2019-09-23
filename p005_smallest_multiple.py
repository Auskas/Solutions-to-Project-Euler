# 
# Solution to Project Euler Problem 5 Smallest multiple.
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Euler
# Don't even try to find the answer by checking every number in the ascending order if it is evenly divisible by all the numbers from 1 to 20.
# That approach takes several dozen seconds. There is a more elegant algorithm. First of all, a number that is evenly divisible by a set of numbers is called
# the Least Common Multiple (LCM) of those numbers. The LCM of any two numbers (a,b) can be found as (a * b) / GCD(a, b), where GCD is the Greatest Common Divisor.
# The LCM of more than two numbers can be found as lcm(a1,a2,a3,...an) = lcm(lcm(a1,a2,a3,...an-1),an) and so on.

import time

def lcm(a=2,b=3):
    """ Gets two numbers a=2 and b=2. Returns the Least Common Divisor of the numbers from 2 to 20 inclusive."""
    if b == 20:
        return int((a * b) / gcd(a, b))
    return lcm((a * b) / gcd(a, b), b + 1)

def gcd(a,b,div=2,common_divisor=1):
    """ Gets two numbers a and b. Returns the Greatest Common Divisor of these numbers."""
    if div > b:
        return common_divisor
    if a % div == 0 and b % div == 0:
        common_divisor = div
    return gcd(a, b, div + 1, common_divisor)

st_time = time.perf_counter()
print("{0} is the smallest number that is evenly divisible by all the numbers from 1 to 20.".format(lcm()))
print("The execution time is {0} seconds.".format(round(time.perf_counter() - st_time,3)))
