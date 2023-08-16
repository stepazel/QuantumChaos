from find_roots import find_roots
import numpy as np
from numpy import sin


e = [np.pi, np.e, np.sqrt(2), np.log(2), 1.98712, np.sqrt(5), np.sqrt(np.e), np.log(5), np.sqrt(np.pi), 0.97127, np.sqrt(3), np.log(3), np.log(np.pi), 1.52321, 0.86127] # final
# e = [np.pi, np.e, np.sqrt(5), 2.5]# 4 edges
# e = [np.pi, np.e, np.sqrt(5), 2.5, np.log(5), np.pi**3] # 6 edges
# e = [np.pi, np.e, np.sqrt(5), np.pi**3] # 1 edge larger than the others
# e = [1, 2, 3, 4, 5, 6] # rationally dependent edge lengths



def func(k: float) -> float:
    return sin(e[0] * k) \
           * sin(e[1] * k) \
           * sin(e[2] * k) \
           * sin(e[3] * k) \
           * sin(e[4] * k) \
           * sin(e[5] * k) \
           * sin(e[6] * k) \
           * sin(e[7] * k) \
           * sin(e[8] * k) \
           * sin(e[9] * k) \
           * sin(e[10] * k) \
           * sin(e[11] * k) \
           * sin(e[12] * k) \
           * sin(e[13] * k) \
           * sin(e[14] * k) \



if __name__ == '__main__':
    roots = find_roots(func, 1_000_000)
    np.save(f'roots2', roots)
