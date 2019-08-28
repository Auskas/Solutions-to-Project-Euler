# 
# Solution to Project Euler Problem 94 Almost equilateral triangles.
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Euler
# 
# The basic idea is the following: the area of an almost equilateral triangle equals to A = (a * h) / 2,
# where a is the base (the side that differs), h - is the height of the base.
# The height must be an integer. The height divides any equilateral triangle into two equal right-angled triangles.
# The right-angled triangles must have integer sides.
# Therefore, the sides form the well-known Pythogorean triple.
# The formulas for finding the sides: a = m ** 2 - n ** 2, b = 2 * m * n, c = m ** 2 + n ** 2, where n < m.
# If c minus the double minimum of a and b equals to +-1, then there is m and n that solve the equation.
# Starting with 2 the program increament m by 1 and seeks for n to let the above-mentioned happens.

import time

# If a < b, then c - a = +- 1, i.e. m ** 2 + n ** 2 - 4 * m * n = +-1
# The following function solves the equation for known m.
def quadratic_equation1(b,c):
    """ Gets the coefficients b and c of the quadratic equation x ** 2 - b * x + c = 0. Finds the descriminant.

    Returns the minimum integer root of the equation if it exists. Otherwise, retruns False."""
    D = b ** 2 - 4 * c
    # If the discriminant is negative, there is no real roots. The square root of the discriminant must be an integer to have integer roots.
    if D < 0 or D ** (1/2) - int(D ** (1/2)) > 0:
        return False
    elif D == 0:
        return int(b/2)
    # If the discriminant is positive there are two roots, we need the lowest one.
    else:
        return min(int((b + D ** (1/2)) / 2),int((b - D ** (1/2)) / 2))

# If b < a, then c - b = +- 1, i.e. 3 * n ** 2 - m ** 2 = +-1
# The following function solves the equation for known m.
def quadratic_equation2(c):
    """ Gets the coefficient c of the quadratic equation 3 * n ** 2 = c.

    Returns the positive integer root of the equation if it exists. Otherwise, returns False."""
    if c % 3 > 0 or (c / 3) ** (1/2) - int((c / 3) ** (1/2)) > 0:
        return False
    return int((c / 3) ** (1/2))

def triangles_searching(m=2,sum_of_perimeters=0):
    """ Starting with two increaments m by one and determines if there is n that let to form an almost equilateral triangle with integer side lengths and the area.

    Returns the sum of perimeters of those triangles for the perimeters below one billion."""
    while True:
        # The square root of 333 333 333 (the maximum length of an almost equilateral triangle to have the perimeter less than one billion) is roughly 18257.
        if m > 18258:
            break
        # The following four conditions checks if there is a proper n for given m to form a equilateral triangle with all integral side lenghts and the area.
        # The following two conditions could work if 2 * m * n < m ** 2 - n ** 2.
        if quadratic_equation1(4 * m, m ** 2 + 1):
            n = quadratic_equation1(4 * m, m ** 2 + 1)
        elif quadratic_equation1(4 * m, m ** 2 - 1):
            n = quadratic_equation1(4 * m, m ** 2 - 1)
        # The following two conditions could work if m ** 2 - n ** 2 < 2 * m * n.
        elif quadratic_equation2(m ** 2 + 1):
            n = quadratic_equation(m ** 2 + 1)
        elif quadratic_equation2(m ** 2 - 1):
            n = quadratic_equation2(m ** 2 - 1)
        # There is no solutions for the current m.
        else:
            m += 1
            continue
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2
        sum_of_perimeters += (min(a,b) * 2 + 2 * c)
        m += 1
    return sum_of_perimeters

st_time = time.perf_counter()
print("The sum of the perimeters of all the so-called almost equilateral triangles with integral side lengths and area",end=" ")
print("and whose perimeters do not exceed one billion equals to", triangles_searching())
print("The execution time is {0} seconds.".format(time.perf_counter() - st_time))
