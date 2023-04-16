import numpy as np
import matplotlib.pyplot as plt
from complete_graph_matrix import edge_lengths
from plots import normalize_root
from plots import goe, gue

roots = np.load('5complete_graph_roots100000.npy')


#TODO zkusit jine delky hran (staci pro mene korenu) - to musim u lipiho
# take zkusit stejny determinant jako doposud ale neudelat tu chybu s e a E
# potom zkusit ten dirichlet graf (6 sinu) = mel by byt poisson
# take dat do kupy ten kod a nasdilet ho (jak, notebook?)
# nakonec hlavne psat!!!! nebat se, psat hodne a o hodne tematech

edge_lengths_sum = sum(edge_lengths)
normalized_roots = list(map(lambda root: normalize_root(root, edge_lengths_sum), roots))
sorted_normalized_roots = np.sort(normalized_roots)
spacings = np.diff(sorted_normalized_roots)

plt.hist(spacings, 250, density=True)
x = np.arange(0, 5, 0.05)
plt.plot(x, goe(x), label='GOE')
plt.xlabel('Normalized nearest-neighbor spacings')
plt.ylabel('Frequency')
plt.xlim(xmin=0, xmax=5)
plt.legend()
plt.title('Histogram for a K5 graph')
plt.savefig('K5c')
plt.show()
