# 
# Solution to Project Euler Problem 66 Diophantine equation.
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Euler
# The solution uses a bit modified brute force approach.
# Browses through all possible numerators from 1 to 428571.
# The denominator for each numerator is chosen in order to make the fraction as close as possible to 3/7.
# Next, the denominator is reduced by one cyclically until the fraction is bigger than 3/7.
# The difference between the fraction and 3/7 is compaired with the minimum values.


import time

def fraction_searching(min_n=1, min_d=7):
    """ The function calculates the numerator and denominator of a fraction to the left of 3/7
    in a set of reduced proper fractions in ascending order n/d, where n < d and d < 1 000 000.
    Returns both the numerator and denominator."""
    # The upper limit 428571 of the numerator can be calculated from the inequality n / d < 3 / 7. Therefore, 7 * n < 3 * d.
    # Thus, n < (3 * 1000000) / 7. 1000000 is the maximum value of the denominator.
    for n in range(1, 428572):
        # We want to choose the denominator that way to make the fraction n/d as close to 3/7 as possible; it helps to reduce the number of calculations.
        # One way to do that is to reduce 3/7 by some number (fraction). For example, n / d = 3/7 - 1/d. Thus, (n + 1) / d = 3 / 7. Consequently, d = 7 * (n + 1) / d
        d = int(7 * (n + 1) / 3)
        d_prev = d
        # As soon as the following inequality doesn't work, it means that we jump over 3/7 and the fraction n / d becomes bigger than 3/7.
        # d_prev is used to get back to the value of the denominator so the fraction n/d is less than 3/7.
        while 7 * n - 3 * d < 0:
            d_prev = d 
            d -= 1
        if min_n * d_prev < min_d * n:
            min_n, min_d = n, d_prev
    return min_n, min_d

st_time = time.perf_counter()
n, d = fraction_searching()
print("The fraction {0} / {1} stands immediatelly to the left of the fraction 3/7 in a set of reduced proper fractions in ascending order n/d, where n < d and d < 1 000 000.".format(n,d))
print("The execution time is {0} seconds.".format(time.perf_counter() - st_time))
