from typing import Callable
from scipy.optimize import root_scalar
import time

tol = 1e-8


# rovnice bude soucit 6 sinu proste (vsude dirichlet)

def find_roots_in_interval(func: Callable, interval_size: int, precision: int, method: str = 'brentq') -> list:
    roots = []
    i = 0
    tic = time.perf_counter()

    for i in range(interval_size * precision):
        # specify the interval for the current iteration
        a = i / precision
        b = a + 1 / precision
        interval = [a, b]
        if func(a) * func(b) > 0:
            i += 1
            continue
        # find the root in the current interval
        result = root_scalar(func, bracket=interval, xtol=tol, method=method)
        # check if the root is not already in the list of roots and append it
        if abs(result.root) > tol and abs(result.root - interval[1]) > tol and abs(result.root - interval[0]) > tol:
            roots.append(result.root)
        i += 1
        if len(roots) % 10_000 == 0:
            print(len(roots))
    toc = time.perf_counter()
    print(f"Elapsed time {toc - tic:0.4f} seconds")
    return roots


# TODO try a more efficient algorithm
# use paralellization
# use analytical derivates??

def find_roots(func: Callable, number_of_roots: int, precision=400) -> list:
    roots = []
    i = 0
    tic = time.perf_counter()
    percentage = 0

    while len(roots) < number_of_roots:
        a = i / precision
        b = a + 1 / precision
        interval = [a, b]
        if func(a) * func(b) > 0:
            i += 1
            continue
        # find the root in the current interval
        result = root_scalar(func, bracket=interval, xtol=tol, method='brentq')
        # check if the root is not already in the list of roots and append it
        if abs(result.root) > tol and abs(result.root - interval[1]) > tol and abs(result.root - interval[0]) > tol:
            roots.append(result.root)
        i += 1
        if len(roots) % (number_of_roots / 100) == 0:
            print(f"{percentage}% completed")
            percentage += 1
    toc = time.perf_counter()
    print(f"Elapsed time {toc - tic:0.4f} seconds")
    print(f"Ending was at {i / precision}")
    return roots
