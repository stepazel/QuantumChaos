import numpy as np
import matplotlib.pyplot as plt
from roots import e
from plots import normalize_root
from plots import poisson

if __name__ == '__main__':
    roots = np.load('roots1.npy')

    edge_lengths_sum = sum(e)
    normalized_roots = list(map(lambda root: normalize_root(root, edge_lengths_sum), roots))
    sorted_normalized_roots = np.sort(normalized_roots)
    spacings = np.diff(sorted_normalized_roots)

    plt.hist(spacings, 150, density=True)
    x = np.arange(0, 5, 0.05)
    plt.plot(x, poisson(x), label='Poisson')
    plt.xlabel('Normalized nearest-neighbor spacings')
    plt.ylabel('Frequency')
    plt.xlim(xmin=0, xmax=5)
    plt.legend()
    plt.title('Histogram for a Dirichlet star graph')
    plt.savefig('graph')
    plt.show()
