import numpy as np
import matplotlib.pyplot as plt
from complete_graph_matrix import edge_lengths
from plots import normalize_root
from plots import goe, gue

roots = np.load('complete_graph_5/5complete_graph_roots100000.npy')

edge_lengths_sum = sum(edge_lengths)
normalized_roots = list(map(lambda root: normalize_root(root, edge_lengths_sum), roots))
sorted_normalized_roots = np.sort(normalized_roots)
spacings = np.diff(sorted_normalized_roots)

plt.hist(spacings, 250, density=True)
x = np.arange(0, 5, 0.05)
plt.plot(x, gue(x), label='GUE')
plt.xlabel('Normalized nearest-neighbor spacings')
plt.ylabel('Frequency')
plt.xlim(xmin=0, xmax=5)
plt.legend()
plt.title('Histogram for a K5 graph')
plt.savefig('K5a')
plt.show()
