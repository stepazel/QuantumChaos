from typing import Callable
from scipy.optimize import root_scalar
import time

# \cos\left(ax\right)\sin\left(bx\right)\sin\left(cx\right)\sin\left(dx\right)\sin\left(fx\right)\sin\left(gx\right)\ +\ \cos\left(bx\right)\sin\left(ax\right)\sin\left(cx\right)\sin\left(dx\right)\sin\left(fx\right)\sin\left(gx\right)+\cos\left(cx\right)\sin\left(bx\right)\sin\left(ax\right)\sin\left(dx\right)\sin\left(fx\right)\sin\left(gx\right)\ +\ \cos\left(dx\right)\sin\left(cx\right)\sin\left(bx\right)\sin\left(ax\right)\sin\left(fx\right)\sin\left(gx\right)\ +\ \cos\left(fx\right)\sin\left(dx\right)\sin\left(cx\right)\sin\left(bx\right)\sin\left(ax\right)\sin\left(gx\right)\ +\ \cos\left(gx\right)\sin\left(fx\right)\sin\left(dx\right)\sin\left(cx\right)\sin\left(bx\right)\sin\left(ax\right)
# https://www.desmos.com/calculator/vfk5v72yl3

tol = 1e-8


def find_roots_in_interval(func: Callable, interval_size: int, precision: int) -> list:
    roots = []
    i = 0
    tic = time.perf_counter()

    for i in range(interval_size * precision):
        # while len(roots) < 1_000_000:
        # specify the interval for the current iteration
        a = i / precision
        b = a + 1 / precision
        interval = [a, b]
        if (func(a)*func(b) > 0):
            i += 1
            continue
        # find the root in the current interval
        result = root_scalar(func, bracket=interval, xtol=tol)
        # check if the root is not already in the list of roots and append it
        if abs(result.root) > tol and abs(result.root - interval[1]) > tol and abs(result.root - interval[0]) > tol:
            roots.append(result.root)
        i += 1
        if (len(roots) % 10_000 == 0):
            print(len(roots))
    toc = time.perf_counter()
    print(f"Elapsed time {toc-tic:0.4f} seconds")
    return roots


def find_roots(func: Callable, number_of_roots: int) -> list:
    roots = []
    i = 0
    tic = time.perf_counter()
    percentage = 0
    precision = 400

    while (len(roots) < number_of_roots):
        a = i / precision
        b = a + 1 / precision
        interval = [a, b]
        if (func(a)*func(b) > 0):
            i += 1
            continue
        # find the root in the current interval
        result = root_scalar(func, bracket=interval, xtol=tol)
        # check if the root is not already in the list of roots and append it
        if abs(result.root) > tol and abs(result.root - interval[1]) > tol and abs(result.root - interval[0]) > tol:
            roots.append(result.root)
        i += 1
        if (len(roots) % (number_of_roots / 100) == 0):
            print(f"{percentage}% completed")
            percentage += 1
    toc = time.perf_counter()
    print(f"Elapsed time {toc-tic:0.4f} seconds")
    print(f"Ending was at {i / precision}")
    return roots
        