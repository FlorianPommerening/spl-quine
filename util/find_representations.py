#!/usr/bin/env python3

import quine
from collections import Counter
from itertools import product

import math


# Brute force attempt to find good constants


def get_frequencies():
    pre = quine.prefixsection.generate()
    code = quine.codesection.generate(pre)
    from collections import Counter
    return Counter(code)


def find_representations(fixed_constants, weights):
    rep = dict((ord(c), (float("inf"), None)) for c in weights)
    # Assume cost of 4 for all fixed constants
    constants = dict((c, (4, "constant_%s" % c)) for c in fixed_constants)
    # Assume length of 5 for all adjectives and length 4 for the noun
    # used to generate powers of two. (add one to each adjective for spaces)
    for k in range(10):
        if 2**k not in constants:
            constants[2**k] = (6*k+4, "power_of_two_%s" % 2**k)
        if -2**k not in constants:
            constants[-2**k] = (6*k+4, "negative_power_of_two_%s" % 2**k)
    # constants
    rep.update(constants)

    uncovered_numbers = set(ord(c) for c in weights if ord(c) not in constants)
    while uncovered_numbers or changes:
        def add_number(x, cost, r):
            if x < 10000 and (x not in rep or rep[x][0] > cost):
                rep[x] = (cost, r)
                changes = True
        changes = False
        known_numbers = [(x, (cost, r)) for x, (cost, r) in rep.items()
                                          if cost < float("inf")]
        for x, (cost, r) in known_numbers:
            # twice x
            add_number(2*x, cost + 6, "twice " + r)
            # the cube of x
            add_number(x**3, cost + 12, "the cube of " + r)
            # the square of x
            add_number(x**2, cost + 14, "the square of " + r)
            if x > 0:
                # the factorial of x
                add_number(math.factorial(x), cost + 17, "the factorial of " + r)
                # the square root of x
                add_number(int(x**0.5), cost + 19, "the square root of " + r)

        for x1, (cost1, r1) in known_numbers:
            for x2, (cost2, r2) in known_numbers:
                # the sum of x and y
                add_number(x1 + x2, cost1 + cost2 + 16, "the sum of %s and %s" % (r1, r2))
                # the product of x and y
                add_number(x1 * x2, cost1 + cost2 + 20, "the product of %s and %s" % (r1, r2))
                # the difference between x and y
                add_number(x1 - x2, cost1 + cost2 + 28, "the difference between %s and %s" % (r1, r2))

        uncovered_numbers -= set(x for x, (cost, _) in rep.items()
                                       if cost < float("inf"))
    return rep


def main():
    frequencies = get_frequencies()
    frequencies.update("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890")
    constants = [ord(c) for c, _ in frequencies.most_common(3)]
    best = None
    best_cost = float("inf")
    ints_to_cover = [ord(c) for c in frequencies]

    for c1 in range(1, 150):
        for c2 in range(c1 + 1, 150):
            print(c1,c2)
            representations = find_representations(constants + [c1, c2], frequencies)
            cost = sum(c * frequencies[chr(k)] for k, (c, _) in representations.items()
                                                    if k in ints_to_cover)
            if cost < best_cost:
                best_cost = cost
                best = representations

    for char, (cost, rep) in best.items():
        if char in ints_to_cover:
            print("    %s: \"%s\",%d" % (char, rep, cost))


if __name__ == "__main__":
    main()
