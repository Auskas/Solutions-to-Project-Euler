# 
# Solution to Project Euler Problem 6 Sum square difference
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Eulerimport time
# Well, the problem can be solved by calculating every square from 1 to 100 and summing them up as well as finding the sum of the natural numbers and the square of the result.
# However, there are some nice formulas which can faciliate the calculations: the sum of the first n natural numbers is n*(n+1).
# The sum of the squares can be found from (2n + 1)(n + 1)n / 6.

import time

def difference(n=100):
    """ Gets an integer number n. Returns the difference between the sum of the squares
    of the first n natural numbers and the square of the sum."""
    square_of_sum = (n * (n + 1) / 2) ** 2
    sum_of_squares = ((2 * n + 1) * (n + 1) * n) / 6
    return int(square_of_sum - sum_of_squares)

st_time = time.perf_counter()
print("The difference between the sum of the squares of the first {0} natural numbers and the square of their sum equals to {1}.".format(100, difference()))
print("The execution time is {0} seconds.".format(round(time.perf_counter() - st_time, 3)))
