import numpy as np
import matplotlib.pyplot as plt
from matrix import edge_lengths
from distributions import normalize_root
from distributions import goe, gue

roots = np.load('roots500.npy')

edge_lengths_sum = sum(edge_lengths)
normalized_roots = list(map(lambda root: normalize_root(root, edge_lengths_sum), roots))
sorted_normalized_roots = np.sort(normalized_roots)
spacings = np.diff(sorted_normalized_roots)

plt.hist(spacings, 50, density=True)
x = np.arange(0, 5, 0.05)
plt.plot(x, goe(x), label='GOE')
plt.xlabel('Normalized nearest-neighbor spacings')
plt.ylabel('Frequency')
plt.xlim(xmin=0, xmax=5)
plt.legend()
plt.title('Histogram for a K6 graph')
plt.savefig('K6B')
plt.show()
