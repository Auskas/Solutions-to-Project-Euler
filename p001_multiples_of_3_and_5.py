# 
# Solution to Project Euler Problem 1 Multiples of 3 and 5
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Euler
# The module has three functions which do pretty the same thing - calculate the sum of all the multiples of 3 or 5 below N.

import time

# As long as N is a small number, we may simply use the brute force.
def sum_of_multiples(N,sum=0):
    """Returns the sum of all the multiples of 3 or 5 below N."""
    for i in range(3, N):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

# For bigger numbers instead of checking every integer number below N we sums up the multiples in two cycles.
# Using the function range(start,stop,step) we sums up all the numbers divisible by 3 and then all the numbers divisible by 5.
# In the second case we must check if the number is divisible by 3 in order to avoid double sums.
def sum_of_multiples_alt(N,sum=0):
    """Returns the sum of all the multiples of 3 or 5 below N."""
    for i in range(3, N, 3):
        sum += i
    for j in range(5, N, 5):
        if j % 3 != 0:
            sum += j
    return sum

# The fastest way, especially for extremely big N, is the usage of the formula of the sum of the members of an arithmetic progression.
# Sn = n*(a1+an)/2
# We calculate the sum of the progression 3,6,... ((N-1) // 3)*3, add the similar sum of 5,10,15...
# And finally, all we need to do is to deduct the sum of the progression 15,30,45 ...
# That final step is mandatory because we must exclude all the numbers that are divisible by both 3 and 5.
def sum_of_progression(N):
    """Returns the sum of all the multiples of 3 or 5 below N."""
    N -= 1
    divisible_by_three = (N // 3) * (3 + (N // 3) * 3) / 2
    divisible_by_five = (N // 5) * (5 + (N // 5) * 5) / 2
    divisible_by_fifteen = (N // 15) * (15 + (N // 15) * 15) / 2
    return int(divisible_by_three + divisible_by_five - divisible_by_fifteen)

if __name__ == "__main__":
    N = 1000
    start = time.perf_counter()
    print("The sum of all the multiples of 3 or 5 below", N,"is", sum_of_multiples(N))
    print("The execution time is", time.perf_counter() - start,"seconds.")
    start = time.perf_counter()
    print("The sum of all the multiples of 3 or 5 below", N,"is", sum_of_multiples_alt(N))
    print("The execution time is", time.perf_counter() - start,"seconds.")
    start = time.perf_counter()
    print("The sum of all the multiples of 3 or 5 below", N,"is", sum_of_progression(N))
    print("The execution time is", time.perf_counter() - start,"seconds.")


