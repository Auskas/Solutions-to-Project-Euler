# 
# Solution to Project Euler Problem 91 Right triangles with integer coordinates.
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Euler
# There are two functions named obvious and less_obvious. The first one uses the brute force, the second one is a bit modified version of the brute force.
# The second approach is roughly two times faster.

import time

def obvious(counter=0):
    """ Returns the number of right-angled triangles that can be formed in a grid 50 x 50. All the triangles have the origin O(0,0)."""
    for x1 in range(51):
        for y1 in range(1,51):
            for x2 in range(x1,51):
                if x2 == 0 and x1 == 0:
                    continue
                for y2 in range(y1 + 1):
                    # The condition checks if the coordinates x1,y1 equals to x2,y2, therefore it is not a triangle but a line from O(0,0) to P=Q=(x1,y1)=(x2,y2).
                    if x1 == x2 and y1 == y2:
                        continue
                    # The condition checks if it is a right-angled triangle with the right angle at the O(0,0).
                    if x1 == 0 and y2 == 0:
                        counter += 1
                        continue
                    side1_square = x1 ** 2 + y1 ** 2
                    side2_square = (x2 - x1) ** 2 + (y2 - y1) ** 2
                    side3_square = x2 ** 2 + y2 ** 2
                    triangle = [side1_square, side2_square, side3_square]
                    # In order to know which side of a triangle is a hypothetical hypotenuse we sort the squares of the sides. Hypotenuse is the biggest.
                    triangle.sort()
                    if triangle[0] + triangle[1] == triangle[2]:
                        counter += 1
    return counter

# The approach below starts with the counter equals to 7500: there are 50 * 50 triangles with the right angle at the origin O(0,0),
# 50 * 50 triangles when x1 = x2, and 50 * 50 triangles when y1 = y2.
def less_obvious(counter=7500):
    """ Returns the number of right-angled triangles that can be formed in a grid 50 x 50. All the triangles have the origin O(0,0)."""
    for x1 in range(50):
        for y1 in range(1,51):
            for x2 in range(x1 + 1, 51):
                for y2 in range(y1):
                    # The following two conditions check if there is the right angle at one of the coordinates (x1,y1) and (x2,y2).
                    if x1 ** 2 + y1 ** 2 == x1 * x2 + y1 * y2:
                        counter += 1
                    if (x2 ** 2) + (y2 ** 2) - (x1 * x2) - (y1 * y2) == 0:
                        counter += 1
    return counter

st_time = time.perf_counter()
print("The brute force solution:")
print("There are {0} right-angled triangles in a grid 50*50 with the origin O(0,0).".format(obvious()))
print("The execution time is {0} seconds.".format(time.perf_counter() - st_time))
st_time = time.perf_counter()
print("The modified brute force:")
print("There are {0} right-angled triangles in a grid 50*50 with the origin O(0,0).".format(less_obvious()))
print("The execution time is {0} seconds.".format(time.perf_counter() - st_time))
        

 
