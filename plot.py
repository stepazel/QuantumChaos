import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from plots import normalize_root
from plots import goe, gue


def plot_nnd(roots: list, edge_lengths_sum: float, title: str, fig_name: str, bins: int = 100):
    # roots = np.load('5complete_graph_roots10000.npy')

    # edge_lengths_sum = sum(edge_lengths2)
    normalized_roots = list(map(lambda root: normalize_root(root, edge_lengths_sum), roots))
    sorted_normalized_roots = np.sort(normalized_roots)
    spacings = np.diff(sorted_normalized_roots)

    plt.hist(spacings, bins, density=True)
    x = np.arange(0, 5, 0.05)
    plt.plot(x, goe(x), label='GOE')
    plt.xlabel('Normalized nearest-neighbor spacings')
    plt.ylabel('Frequency')
    plt.xlim(xmin=0, xmax=5)
    plt.legend()
    plt.title(title)
    plt.savefig(fig_name)
    plt.show()
