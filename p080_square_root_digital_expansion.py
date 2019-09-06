# 
# Solution to Project Euler Problem 80 Square root digital expansion.
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Euler
# There is a simple recursive algorithm for digit-by-digit calculation of the square root of a number.
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Digit-by-digit_calculation

import time

def x_determination(p,c):
    """ Gets two integer numbers p and c of the inequality x*(20*p + x) <= c. Determines the greatest digit x.
    
    x must be a digit, not a number. Returns the value of x."""    
    for x in range(1,10):
        if x * (20 * p + x) < c:
            continue
        return x - 1
    return 9

def square_root_expansion(c,counter=100,p=0,digital_sum=0):
    """ Gets an integer number c which is not one of the perfect squares. Generates first one hundred digits of the square root.

    Returns the sum of the first one hundred digits of the square root of the number."""
    if counter == 0:
        return digital_sum
    x = x_determination(p,c)
    digital_sum += x
    y = x * (20 * p + x)    
    p = p * 10 + x
    remainder = c - y
    c = remainder * 100
    return square_root_expansion(c,counter-1,p,digital_sum)

st_time = time.perf_counter()   
squares = {i ** 2 for i in range(2,10)}
sum_of_digits = 0
for i in range(2,100):
    # If the number is one of the perfect squares we must skip it according to the requirement of the problem.
    if i in squares:
        continue
    sum_of_digits += square_root_expansion(i)
print("The total of the digital sums of the first one hundred decimal digits"
      "for all the irrational square roots of the first one hundred natural numbers equals to", sum_of_digits)
print("The execution time is {0} seconds.".format(time.perf_counter() - st_time))
