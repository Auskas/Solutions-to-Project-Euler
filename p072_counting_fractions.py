# 
# Solution to Project Euler Problem 72 Counting fractions.
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Euler
# It can be seen that the obvious way to solve the problem is to calculate the Euler's totient function for each n in range from 2 to 1000000.
# However, the upper mentioned approach is extremely slow. There is another elegant way to solve the problem.
# In mathematics a set of proper reduced fractions in ascending order of size is called the Farey sequence.
# The article on Wikipedia provides one with the formula to calculate the length of the sequence.
# The solution to the problem becomes surprisingly short using the knowledge of Farey sequence.

import time

def farey(n):
    """ Gets an integer number n. Returns the number of proper reduced fractions between 0 and 1 not inclusively.
    The value of the denominator ranged between 2 and n inclusively."""
    # The function is recursive. In order to avoid recalculations of the same values, a dictionary of Farey sequence lengths is used.
    # If the value is already evaluated, the function returns the value for that given n.
    if farey_values.get(n):
        return farey_values.get(n)
    # The formula below represents the Farey sequence length formula. After each calculation the value is written into the dictionary.
    farey_values[n] = n * (n + 3) // 2 - sum(farey(n // d) for d in range(2, n + 1))
    return farey_values[n]

farey_values = {}
st_time = time.perf_counter()
# The Farey's formula also includes two extreme cases 0/1 and 1/1. That is why we need to substract 2 from the result.
print("The number of proper reduced fractions in the Farey sequence for N = 1000000 equals to {}.".format(farey(1000000) - 2))
print("The execution time is {0} seconds.".format(time.perf_counter() - st_time))

