import numpy as np
from find_roots import find_roots
from mathematica import get_func_from_mathematica

# ending interval 6762.495 for 100_000 roots!!
# weyl's law : 93775 for this interval


func = get_func_from_mathematica('det_k5.txt')

if __name__ == '__main__':
    num = 10000
    roots = find_roots(func, num, 200)
    np.save(f"5complete_graph_roots{num}", roots)



