# 
# Solution to Project Euler Problem 86 Cuboid route.
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Euler
#
# The first step to solve the problem is to unfold the pictured cuboid. The shortest path is the hypotenuse of the right-angled triangle.
# One of the sides is the length of the cuboid, the other side is the sum of the width and the heigth.
# The algorithm is simple: we calculates the number of solutions for each M starting with 3. Sums up the number of solutions.
# In order to find the number of solutions for each M, we check if there is the number N to form a right-angled triangle with all integer side lengths.

import time

def number_of_cuboids(M=2,counter=0,target=1000000):
    # Here is a little trick: in order to get rid of finding the square root in the Pythagorean theorem
    # the squares of integers are precalculated. At first, I chose the upper limit 10000.
    # However, as soon as I got the answer, the limit was chosen close to the answer multiplied by 2.
    # (We need to take into account the doubled limit because N (the width plus the height) can take values up to 2 * M)
    squares = set([i ** 2 for i in range(2, 4000)])
    while counter < target:
        M += 1
        for N in range(3, 2 * M + 1):
            if M ** 2 + N ** 2 in squares:
                # If the width plus the height of a cuboid is less than the length, there are N // 2 solutions.
                # For instance, if the length (M) equals to 8 and the width plus the height (N) equals to 6, there are 3 solutions:
                # (8,1,5), (8,2,6), (8,3,3). We cannot include (8,5,1), (8,2,6) because those are rotations of the cuboids.
                if N <= M:
                    counter += N // 2
                # If the sum of height and width (N) is bigger than the length (M), the height can take the values between
                # 1 and M inclusive. For instance, if M = 6, N = 8, there are 3 solutions (6,6,2), (6,5,3), (6,4,4).
                else:
                    counter += 1 + (M - (N + 1) // 2)
    return M

st_time = time.perf_counter()
print("The value of M when the number of solutions first exceed one million equals to", number_of_cuboids())
print("The execution time is {0} seconds.".format(time.perf_counter() - st_time))
