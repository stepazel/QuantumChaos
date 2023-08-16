import time
import numpy as np
from skrmt.ensemble import GaussianEnsemble
import matplotlib.pyplot as plt
from distributions import goe, gue, gse
from unfolding import F

functions = {
    1: ("GOE", goe),
    2: ("GUE", gue),
    4: ("GSE", gse),
}

beta = 1
n = 1000
reps = 1000
spacings = []

tic = time.perf_counter()
for r in range(reps):
    matrix = GaussianEnsemble(beta=beta, n=n,
                              use_tridiagonal=True).matrix
    sorted_eigen_values = np.sort(np.linalg.eigvalsh(matrix))
    unfolded_values = [F(eigenvalue, n, beta) for eigenvalue in
                       sorted_eigen_values]
    spacings.extend(np.diff(unfolded_values))

mean = np.mean(spacings)
normalized_spacings = list(map(lambda s: s / mean, spacings))
print(mean)
toc = time.perf_counter()
print(f'Elapsed time: {toc - tic:0.4f} seconds')

np.save(f"{functions[beta][0]}{n}x{n} unfolded and normalized",
        normalized_spacings)

plt.hist(spacings, bins=100, density=True)
x = np.arange(0, 5, 0.05)
plt.plot(x, functions[beta][1](x), label=functions[beta][0])
plt.legend()
plt.xlabel("Normalized spacings of eigenvalues")
plt.ylabel("Frequency")
plt.xlim(xmin=0, xmax=5)
plt.title(f'Histogram for {functions[beta][0]} matrix n={n}')
plt.savefig(functions[beta][0])
plt.show()
