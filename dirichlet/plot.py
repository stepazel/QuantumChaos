import numpy as np
import matplotlib.pyplot as plt
from roots import e
from plots import normalize_root
from plots import poisson

# e = [np.pi, np.e, np.sqrt(2), np.log(2), 1.98712, np.sqrt(5), np.sqrt(np.e), np.log(5), np.sqrt(np.pi), 0.97127]
if __name__ == '__main__':

    n = 3
    roots = np.load(f'roots{n}.npy')
    # roots.

    edge_lengths_sum = sum(e)
    normalized_roots = list(map(lambda root: normalize_root(root, edge_lengths_sum), roots))
    sorted_normalized_roots = np.sort(normalized_roots)
    spacings = np.diff(sorted_normalized_roots)
    test = np.sort(spacings)[::-1]

    plt.hist(spacings, 150, density=True)
    x = np.arange(0, 8, 0.05)
    plt.plot(x, poisson(x), label='Poisson')
    plt.xlabel('Normalized nearest-neighbor spacings')
    plt.ylabel('Frequency')
    plt.xlim(xmin=0, xmax=8)
    plt.legend()
    plt.title('Histogram for a Dirichlet star graph with one greater edge length')
    plt.savefig(f'graph{n}')
    plt.show()
