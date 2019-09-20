# 
# Solution to Project Euler Problem 4 Largest palindrome product.
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Euler
# Well, nothing to comment actually. I decided to arrange two cycles to find the product of two 3-digit numbers.
# There are some optimizations in the algorithm which are not that necessary. Anyway, it is faster to start from the upper limit of 3-digit numbers.

import time

def palindrome_check(x):
    """ Gets an integer x. Returns True if it is a palindrome. Returns False otherwise."""
    if str(x) == str(x)[::-1]:
        return True
    return False

def largest_palindrome():
    """ Returns the largest palindrome made from the product of two 3-digit numbers."""
    pal = [0]
    for elem1 in range(999, 99, -1):
        # If at least one palindrome is found we may break the outer cycle once the product of elem1 * 999 is bigger than the largest palindrome found so far.
        if elem1 * 999 < max(pal):
            break
        for elem2 in range(999, 99, -1):
            # We may break the inner cycle once the largest found so far palindrome is bigger than elem1 * elem2 because we move downwards.
            if elem1 * elem2 < max(pal):
                break
            if palindrome_check(elem1 * elem2):
                # Additionaly to the task I decided to print the multipliers as well.
                if elem1 * elem2 > max(pal):
                    elems = [elem1, elem2]
                pal.append(elem1 * elem2)
    return max(pal), elems

st_time = time.perf_counter()
largest, elems = largest_palindrome()
print("The largest palindrome made from the product of two 3-digit numbers is", largest)
print("The numbers are {0} and {1}.".format(elems[0], elems[1]))
      
print("The execution time is", round(time.perf_counter() - st_time, 3), "seconds.")    
              
                
