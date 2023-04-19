from find_roots import find_roots
import numpy as np
from numpy import sin

# edges
# e = [np.pi, np.e, np.sqrt(2), np.pi ** 2, 1.486, np.sqrt(np.e)]

e = [np.pi, np.e, np.sqrt(2), np.log(2), 0.5772156649, np.sqrt(3)]


def func(k: float) -> float:
    return sin(e[0] * k) * sin(e[1] * k) * sin(e[2] * k) * sin(e[3] * k) * sin(e[4] * k) * sin(e[5] * k)


if __name__ == '__main__':
    roots = find_roots(func, 100_000, 200)
    np.save(f'roots1', roots)
