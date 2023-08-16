import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matrix import edge_lengths2
from distributions import normalize_root
from distributions import goe, gue
from mathematica import get_func_from_mathematica

# func = get_func_from_mathematica('det_k5.txt')

neco = np.load('K5roots499.npy')
roots = [*set(neco)]

# roots.sort()
# del roots[:363]
# roots = list(filter(lambda z: abs(func(z)) < 1e-10, roots1))

# values = [func(root) for root in roots]
edge_lengths_sum = sum(edge_lengths2)
normalized_roots = list(map(lambda root: normalize_root(root, edge_lengths_sum), roots))
sorted_normalized_roots = np.sort(normalized_roots)
spacings = np.diff(sorted_normalized_roots)

plt.hist(spacings, 30, density=True)
x = np.arange(0, 5, 0.05)
plt.plot(x, goe(x), label='GOE')
plt.xlabel('Normalized nearest-neighbor spacings')
plt.ylabel('Frequency')
plt.xlim(xmin=0, xmax=5)
plt.legend()
plt.title('Histogram for a K5 graph')
plt.savefig('K5H')
plt.show()
