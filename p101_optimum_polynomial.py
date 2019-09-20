# 
# Solution to Project Euler Problem 101 Optimum polynomial.
# Copyright (c) Auskas. All rights reserved.
#
# https://github.com/Auskas/Solutions-to-Project-Euler
# There are the so-called Lagrange polynomials used for generating a polynomial function for a given set of points.
# Look at the following article on Wikipedia https://en.wikipedia.org/wiki/Lagrange_polynomial
# Once you have a polynomial for a given set of points you can calculate the next point.
# Sure I could use the module numpy to get the coefficients of polynomials, but I prefer to write my own modules.

import time

st_time = time.perf_counter()

# The polynomials in this problem's case are formed as (x - x1)(x - x2)..(x - xn) depending on the degree of a polynomial.
# The coefficients of the polynom a0 * x ^ 2 + a1 * x + a2 are precalculated. 
# The list roots consists of 3 lists of x1 and x2 (therefore, (x - 1)(x - 2), (x - 1)(x - 3), and (x - 2)(x - 3).
# The coefficients of the corresponding quadratic function are in the list coeffs with the same indicies.
roots = [[1,2],[1,3],[2,3]]
coeffs = [[1,-3,2],[1,-4,3],[1,-5,6]]

def values(n):
    """ Gets an integer n. Returns the value of the polynomial for a given n."""
    y = 1 - n + n ** 2 - n ** 3 + n ** 4 - n ** 5 + n ** 6 - n ** 7 + n ** 8 - n ** 9 + n ** 10
    return y

def basis_polynomials(j,k):
    """ Gets integers j and k to form Lagrange basis polynomial. Returns the coefficients of the interpolation polynomial in the Lagrange form."""
    x = [i for i in range(1,11)]
    denom = 1
    current_roots = []
    for m in range(k):
        if m == j: 
            continue
        current_roots.append(x[m])
        denom *= (x[j] - x[m])
    # If a given set of xm is already found, returns the coefficients. Otherwise, calls the function next_coeffs to obtain them.
    if current_roots in roots:
        return coeffs[roots.index(current_roots)], denom
    return next_coeffs(current_roots), denom

def next_coeffs(current_roots):
    """ Gets a list of the roots of a polynomial of the form (x - x1)(x - x2)...(x - xn). Finds the coefficients of the polynomial.
    Adds the new roots and the coefficients to the corresponding lists. Returns the coefficients."""
    # It is really hard to find the coefficients of polynomials of higher degrees. Nevertheless, if we know the coefficients of (x - x1)(x - x2)...(x - xn),
    # it is a piece of cake to find the coefficients when we add another multiplier (x - xk).
    # Add the new roots to the list, the corresponding coeffs will be added at the end of the function.
    roots.append(current_roots)
    previous = current_roots[:len(current_roots) - 1]
    new_root = current_roots[len(current_roots) - 1]
    i = roots.index(previous)
    # The first coefficient is always 1. The second one is always the sum of x1 to xk and is negative.
    temp = [1, coeffs[i][1] - new_root]
    for j in range(2, len(coeffs[i])):
        temp.append(coeffs[i][j] - new_root * coeffs[i][j-1])
    # The last coefficient is always the product of the roots.
    temp.append(coeffs[i][len(coeffs[i]) - 1] * -new_root)
    # Add the coefficients to the list for further usage.
    coeffs.append(temp)
    return temp

# I manually calculated the FIT for the linear polynomial (it is 682x - 681). Therefore, the sum of the first two FIT's is 1 + 1365. fits = 1366.
def polynomials(y,fits=1366):
    """ Gets a set of points y. Generates proper polynomials for the first k points.
    Calculates the first term of each polynomial when the result doesn't fit the set.
    Returns the sum of the so-called first incorrect terms."""
    for k in range(3,11):
        print("The optimum polynomial generating function for the first {0} terms is the following:".format(k))
        result = [0 for i in range(k)]
        for j in range(k):
            temp_coeffs, denom = basis_polynomials(j,k)
            t = temp_coeffs[:]
            for i in range(k):
                result[i] += y[j] * t[i] / denom
        # Didn't want to drag fractions till the end. That is why I use the function round. I guarantee that small fix gives the right result.
        # The middle of the function is solely dedicated to the printing of the intermeddiate results. Should've got rid of it perhaps.
        print("{0} x^{1}".format(round(result[0]),k-1),end ="")
        pr = k - 2
        for i in range(1, len(result) - 1):
            if result[i] > 0:
                print(" + ", end="")
            else:
                print(" - ", end="")
            print("{0} x ^{1}". format(round(abs(result[i])), pr), end="")
            pr -= 1
        if result[len(result) - 1] > 0:
            print(" + ", end="")
        else:
            print(" - ", end="")
        print(round(abs(result[len(result) - 1])))
        print("The first {0} terms of the optimum polynomial functions are the following:".format(k+1))
        for n in range(1, k + 2):
            power = k - 1
            temp_y = 0
            for elem in result:
                temp_y += elem * n ** power
                power -= 1
            temp_y = round(temp_y)
            if n == k + 1:
                fits += temp_y
            print(temp_y,end=" ")
        print()
        print("{0} is not the {1}th term of the original sequence...".format(temp_y, k+1))
        print()
    return fits


y = [values(n) for n in range(1,12)]
print("The first eleven terms of the original polynomial function are the following:")
for elem in y:
    print(elem, end=" ")
print()
print()
print("The sum of the first incorrect terms of the found polynomial functions is", polynomials(y))
print("The execution time is {0} seconds.".format(time.perf_counter() - st_time))
