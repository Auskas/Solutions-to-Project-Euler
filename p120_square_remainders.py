# 
# Solution to Project Euler Problem 120 Square remainders.
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Euler
# If you expand the numerator of the expression for a couple of values of n, you will notice a pattern.
# For every even n there are only even powers of a with 2 at the end. For instance, if n = 4, the numerator is 2a^4 + 12a^2 + 2.
# Therefore, for every even n the remainder is 2.
# For odd n there are only odd powers of a (there aren't any numbers in the result). For example, if n = 3, the numerator is 2a^3 + 6a.
# Again, we're only interested in the last member of the expression. The values are following (n: k): 1: 2, 3: 6, 5: 10, 7: 14 etc.
# Thus, the formula for calculating the remainder is r = 2na. The remainder cannot be bigger than a^2 - 1.
# Hence, n <= (a^2 - 1) / 2a. Now we know everything to calculate the maximum remainder for every a.

import time

def max_remainder(a):
    """ Gets an integer positive number a.

    Returns the maximum remainder of the following expression ((a - 1) ^ n + (a + 1) ^ n) / a ^ 2"""
    n = int((a ** 2 - 1) / (2 * a))
    r_max = 2 * n * a
    return r_max

st_time = time.perf_counter()
sum_r_max = 0
for a in range(3,1001):
    sum_r_max += max_remainder(a)
print("The sum of the maximum remainders euqals to", sum_r_max)
print("The execution time is {0} seconds.".format(time.perf_counter() - st_time))
