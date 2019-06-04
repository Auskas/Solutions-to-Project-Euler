#
# Solution to Project Euler Problem 2 Even Fibonacci numbers
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Euler
# Only one solution is proposed. It is really fast. I don't believe there is much room for performance improvement.

import time

# The idea is simple - we start with two numbers previous = 1 and current = 1
# We sums up the numbers getting the next Fibonacci sequence member. If the next number is even we add it to the sum.
# Current number becomes the sum, previous number is the old value of the current number.
# When the sum of the current and previous number is bigger than N, we're done.
def even_fibonacci(N,sum=0,previous=1,current=1):
    """Returns the sum of even numbers in the Fibonacci sequence from 1 to N."""
    while previous + current < N:
        current, previous = current + previous, current
        if current % 2 == 0:  
            sum += current      
    return sum

if __name__ == '__main__':
    start = time.perf_counter()
    N = 4000000
    print("The sum of even Fibonacci numbers below", N, "equals to", even_fibonacci(N))
    print("The execution time is", time.perf_counter() - start,"seconds.")
