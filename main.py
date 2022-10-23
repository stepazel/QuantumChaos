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

n = 200
reps = 5000
spacings = []
for r in range(reps):
    matrix = GaussianEnsemble(beta=beta, n=n, use_tridiagonal=True).matrix
    sorted_eigen_values = np.sort(np.linalg.eigvalsh(matrix))
    hmm = [F(eigenvalue, n, 1) for eigenvalue in sorted_eigen_values]
    spacings.extend(np.diff(hmm))
    # if r % 10_000 == 0:
    print(r)

mean = np.mean(spacings)
normalized_spacings = list(map(lambda s: s / mean, spacings))

plt.hist(normalized_spacings, bins=500, density=True)
x = np.arange(0, 5, 0.1)
plt.plot(x, betas[beta][1](x), label=betas[beta][0])
plt.legend()
plt.xlabel("Normalized spacings of eigenvalues")
plt.ylabel("Frequency")
plt.xlim(xmin=0, xmax=5)
plt.title("Histogram for " + betas[beta][0] + " " + str(n) + "x" + str(n))
# plt.savefig(betas[beta][0] + str(n))
plt.show()
