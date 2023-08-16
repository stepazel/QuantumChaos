from typing import Callable
from scipy.optimize import root_scalar
import time

tol = 1e-12


def find_roots_in_interval(func: Callable, interval_size: int,
                           precision: int,
                           method: str = 'brentq') -> list:
    roots = []
    tic = time.perf_counter()

    for i in range(interval_size * precision):
        # specify the interval for the current iteration
        a = i / precision
        b = a + 1 / precision
        interval = [a, b]

        if func(a) * func(b) > 0:
            i += 1
            continue

        result = root_scalar(func, bracket=interval, xtol=tol,
                             method=method)
        if result.converged and result.root not in roots:
            roots.append(result.root)
        i += 1
        if len(roots) % 10_000 == 0:
            print(len(roots))
    toc = time.perf_counter()
    print(f"Elapsed time {toc - tic:0.4f} seconds")
    return roots


def find_roots(func: Callable, number_of_roots: int, precision=400,
               method: str = 'brentq') -> list:
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

        result = root_scalar(func, bracket=interval, xtol=tol,
                             method=method)
        if result.converged and result.root not in roots:
            roots.append(result.root)
        i += 1
        if len(roots) % (number_of_roots / 100) == 0 and len(
                roots) != 0:
            print(f"{percentage}% completed")
            percentage += 1
    toc = time.perf_counter()
    print(f"Elapsed time {toc - tic:0.4f} seconds")
    print(f"Ending was at {i / precision}")
    return roots
