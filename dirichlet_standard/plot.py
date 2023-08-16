import matplotlib.pyplot as plt
import numpy as np
from equations import edge_lengths
from distributions import goe


roots = np.load(f'dirichlet_standard_roots_{100_000}.npy')

# normalize the values
edge_lengths_sum = sum(edge_lengths)
normalized_roots = list(map(lambda root: (root * edge_lengths_sum) / np.pi, roots))
# get spacings
sorted_normalized_roots = np.sort(normalized_roots)
spacings = np.diff(sorted_normalized_roots)

plt.hist(spacings, 150, density=True)
x = np.arange(0, 5, 0.05)
plt.plot(x, goe(x), label='goe')
plt.xlabel('Normalized nearest-neighbor spacings')
plt.ylabel('Frequency')
plt.xlim(xmin=0, xmax=5)
plt.legend()
plt.title('Histogram for a dirichlet-standard graph')
plt.savefig('dirichlet_standard1')
plt.show()