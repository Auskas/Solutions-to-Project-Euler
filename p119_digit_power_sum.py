# 
# Solution to Project Euler Problem 119 Digit power sum.
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Euler
# Instead of checking every number starting from 10 if it satisfies to the condition,
# we should generate powers of integer numbers to see if they satisfy.
# The main function 'dynamic_powers' tracks the current minimum exponent of the dictionary 'powers'.
# If there is the next number immediately after which exponent lower than the minimum of the dictionary,
# it is added to the dictionary. Also, the function removes already used integers from the dictionary.
# Unfortunately, I cannot prove that they won't be used with another power in the sequence.
# However, the empirical run shows that all the bases are different.

import time

def minimum_power(number):
    """ Gets an integer number.
    Returns the minimum power required to get enough digits of 'number ** exponent' so their sum be greater of equal to the number itself.
    For instance, the minimum exponent of 26 is 2 (26 ** 2 = 676 - theoretically, there are enough digits to get the sum 26).
    The minimum exponent of 28 is 3 (28 ** 2 = 784 - the maximum sum of 3 digits is 27)."""
    power = 2
    while number > len(str(number ** power)) * 9:
        power += 1
    return power

def power_sum(number, the_sum=0):
    """ Gets an integer number.

    Returns the sum of its digits."""
    for i in range(len(str(number))):
        the_sum += int(str(number)[i])
    return the_sum
        
def dynamic_powers(counter=0,base=2,power=4):
    """ The function creates an increasing sequence of numbers formed as a base in the power of another integer.
    The base equals to the sum of digits of the base in the power of some integer.
    As soon as it is the 30th number in the sequence, returns it."""
    # The dictionary 'powers' contains the bases (as the keys) and the powers (as the values).
    # As long as the condition demands to use at least two-digit numbers, we skip 2**2, 2**3 and 3**2.
    powers = {2:4, 3:3}
    sequence = set()
    while True:
        # Each cycle the minimum 'base ** power' number from the dictionary is chosen.
        for elem in powers:
            if elem ** powers[elem] < base ** power:
                base, power = elem, powers[elem]
        if power_sum(base ** power) == base and base ** power not in sequence:
            counter += 1
            if counter == 30:
                # It is the 30th number in the sequence.
                return base ** power
            sequence.add(base ** power)
            # Somehow, the bases are always different, therefore, we may get rid of already used one.
            powers.pop(base)
        else:
            # If we can add the next number to the dictionary (if its exponent is lower than the minimum exponent of the dictionary)
            if base ** power > (max(powers) + 1) ** minimum_power(max(powers) + 1):
                powers[max(powers) + 1] = minimum_power(max(powers) + 1)
            # Otherwise, we simply increase the power of the current base.
            else:
                power += 1
                powers[base] = power

st_time = time.perf_counter()
print("The 30th number in the sequence of numbers equal to the sum of its digits raised to some power is", dynamic_powers())
print("The execution time is {0} seconds.".format(time.perf_counter() - st_time))
