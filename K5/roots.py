import numpy as np
from find_roots import find_roots
from mathematica import get_func_from_mathematica

# ending interval 6762.495 for 100_000 roots!!
# weyl's law : 93775 for this interval


# bisection, ending 211, 2000 roots

# 1001 roots, ending 106

func = get_func_from_mathematica('det_k5.txt')

def normalized_func(x):
    original_value = func(x)

    return original_value * 10e69

if __name__ == '__main__':
    num = 499
    roots = find_roots(func, num, 400, method='brentq')
    np.save(f"K5roots{num}", roots)



