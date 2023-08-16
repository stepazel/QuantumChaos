from find_roots import find_roots
from mathematica import get_func_from_mathematica
from numpy import save

func = get_func_from_mathematica('det_k6.txt')

# 100 - 28.44
count = 501
# Elapsed time 35292.1092 seconds
# Ending was at 2418.44
if __name__ == '__main__':
    roots = find_roots(func, count, 200)
    save(f'roots{count}', roots)
# TODO zkusit ty koreny hledat in paralel - treba 6 procesu pro intervaly 0, 10000; 10001, 20000; ... https://stackoverflow.com/questions/7207309/how-to-run-functions-in-parallel