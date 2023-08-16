import numpy as np
import matplotlib.pyplot as plt
from skrmt.ensemble import GaussianEnsemble

labels = {
    1: "GOE",
    2: "GUE",
    4: "GSE",
}

beta = 1
n = 1000
reps = 100_000

eigenvalues = []
for r in range(reps):
    matrix = GaussianEnsemble(beta=beta, n=n,
                              use_tridiagonal=True).matrix
    sorted_eigen_values = np.sort(np.linalg.eigvalsh(matrix))
    eigenvalues.extend(sorted_eigen_values)
    if r % 10_000 == 0:
        print(r)

plt.title(f'{labels[beta]} n={n} eigenvalues')
plt.hist(eigenvalues, bins=200, density=True)
plt.savefig(f'{labels[beta]} n={n} eigenvalues')
plt.show()
