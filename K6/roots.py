from find_roots import find_roots
from mathematica import get_func_from_mathematica
from numpy import save

func = get_func_from_mathematica('det_k6.txt')

# 100 - 28.44
count = 10000
# Elapsed time 35292.1092 seconds
# Ending was at 2418.44
if __name__ == '__main__':
    roots = find_roots(func, count, 200)
    save(f'roots{count}', roots)
