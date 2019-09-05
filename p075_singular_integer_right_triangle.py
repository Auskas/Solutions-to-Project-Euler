# 
# Solution to Project Euler Problem 73 Counting fractions in a range.
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Euler
# Right-angled triangles with all integer sides are also known as Pythagorean triangles.
# The sides can be generated using the Euclid formulae: a = k*(m**2-n**2), b = 2*m*n, c = m**2+n**2,
# where m > n, m and n are coprime and not both odd, k is a positive integer.
# The solution uses two sets of perimeters: all possible perimeter lengths generated with the help of the formulae,
# and a set of perimeters which encounter more than once during the generation.
# The answer is simply the difference between the lengths of the sets.


import time

# The names of the sets are self-explanatory
possible_perimeters = set()
repeated_perimeters = set()

def coprime(m,n):
    """ Gets two positive integer numbers m and n (m > n).

    Returns True if they are coprime, otherwise, returns False."""
    # The function uses the Euclid's algorithm for finding the greatest common divisor. The algorithm is recursive.
    # If the GCD is 1, when the numbers are coprime. If it is greater than 1, when the numbers aren't coprime.
    if n == 0 and m > 1:
        return False
    elif n == 0 and m == 1:
        return True
    return coprime(n, m - n * (m // n))

def perimeters(L,counter=0):
    """ Gets the range of possible integer perimeters. Generates a set of all possible perimeters of right-angled triangles with integer sides.

    Also generates a set of perimeters of right-angled triangles with integer sides which can be formed using more than one set of values of the sides."""
    for m in range(2, int(L ** (1/2)) + 1):
        for n in range(1, m):
            limit = m * (m + n)
            if limit > 750000:
                break
            if coprime(m,n) and ((m - n) % 2 > 0):
                for k in range(1, 750000 // limit + 1):
                    if 2 * k * limit in possible_perimeters:
                        repeated_perimeters.add(2 * k * limit)
                    else:
                        possible_perimeters.add(2 * k * limit)
          
st_time = time.perf_counter()
perimeters(1500000)
print(len(possible_perimeters) - len(repeated_perimeters))
print("The execution time is {0} seconds.".format(time.perf_counter() - st_time))
