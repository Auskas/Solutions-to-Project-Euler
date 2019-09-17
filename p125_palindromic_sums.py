# 
# Solution to Project Euler Problem 125 Palindromic sums.
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Euler
# The algorithm generates the sum of consecutive squares and saves it in a list.
# For instance, after 3 iterations the list consists of [1+4+9+16, 4+9+16, 9+16, 16].
# In each cycle the sum of each already generated sequence of consecutive squares is checked if it is palindromic.

import time

def is_palindrome(x):
    """ Gets an integer number. Returns True if it is palindromic. Otherwise, returns False."""
    # str(x)[::-1] simply reverses the original string.
    if str(x) == str(x)[::-1]:
        return True
    return False

def palindrome_counter(sum_of_palindromes=0,square=2,begin=0):
    """ Counts the sum of the numbers below 100 million that are both palindromic and can be written as the sum of consecutive squares."""
    # There are some numbers that can be written as the different sums of consecutive squares. In order to avoid adding the same numbers we put all found plindromes in the set.
    numbers = set()
    sequences = [1]
    while True:
        s = square ** 2
        for i in range(begin,len(sequences)):
            if sequences[i] + s < 100000000:
                sequences[i] += s
                if is_palindrome(sequences[i]) and sequences[i] not in numbers:
                    sum_of_palindromes += sequences[i]
                    numbers.add(sequences[i])
            else:
                # If the current sum is bigger than 100 million, we don't need it anymore and can start next time from the next sum.
                begin = i + 1
        square += 1
        # The last possible two consecutive squares.
        if s + (square - 1) ** 2 > 100000000:
            break
        sequences.append(s)
    return sum_of_palindromes

st_time = time.perf_counter()

print("The sum of all the numbers below 100 million that are both palindromic and can be written as the sum of consecutive squares is", palindrome_counter())

print("The execution time is {0} seconds.".format(time.perf_counter() - st_time))
