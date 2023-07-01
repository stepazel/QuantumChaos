import time

import numpy as np
from skrmt.ensemble import GaussianEnsemble
import matplotlib.pyplot as plt
from plots import goe, gue, gse
from unfolding import F

betas = {
    1: ("GOE", goe),
    2: ("GUE", gue),
    4: ("GSE", gse),
}

print("""Choose which random matrix from the gaussian ensemble you want to analyze\n
    Beta notation:
    GOE -> 1
    GUE -> 2
    GSE -> 4
""")
beta = int(input("Enter beta notation: "))
if beta not in [1, 2, 4]:
    print("A valid beta has to be selected!")
    exit()
tic = time.perf_counter()

n = 1000
reps = 1000
spacings = []
for r in range(reps):
    matrix = GaussianEnsemble(beta=beta, n=n, use_tridiagonal=True).matrix
    sorted_eigen_values = np.sort(np.linalg.eigvalsh(matrix))
    unfolded_values = [F(eigenvalue, n, beta) for eigenvalue in sorted_eigen_values]
    spacings.extend(np.diff(unfolded_values))
    # spacings.extend(np.diff(sorted_eigen_values))

mean = np.mean(spacings)
normalized_spacings = list(map(lambda s: s / mean, spacings))
print(mean)
toc = time.perf_counter()
print(f'Elapsed time: {toc - tic:0.4f} seconds')

# np.save(betas[beta][0] + " " + str(n) + "x1" + str(n), normalized_spacings)
np.save(f"{betas[beta][0]}{n}x{n} unfolded and normalized", normalized_spacings)
np.save(f"{betas[beta][0]}{n}x{n} unfolded", spacings)

plt.hist(spacings, bins=100, density=True)
x = np.arange(0, 5, 0.05)
plt.plot(x, betas[beta][1](x), label=betas[beta][0])
plt.legend()
plt.xlabel("Normalized spacings of eigenvalues")
plt.ylabel("Frequency")
plt.xlim(xmin=0, xmax=5)
plt.title(f'Histogram for {betas[beta][0]} matrix n={n}')
plt.savefig(betas[beta][0])
plt.show()
