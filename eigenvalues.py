import numpy as np
import matplotlib.pyplot as plt
from skrmt.ensemble import GaussianEnsemble


betas = {
    1: "GOE",
    2: "GUE",
    4: "GSE",
}

print("""Choose which random matrix from the gaussian ensemble you want to analyze\n
    Beta notation:
    GOE -> 1
    GUE -> 2
    GSE -> 4
""")
beta = int(input("Enter beta notation: "))
if (beta not in [1, 2, 4]):
    print("A valid beta has to be selected!")
    exit()

n = 100
reps = 10_000

eigenvalues = []
for r in range(reps):
    matrix = GaussianEnsemble(beta=beta, n=n, use_tridiagonal=True).matrix
    sorted_eigen_values = np.sort(np.linalg.eigvalsh(matrix))
    eigenvalues.extend(sorted_eigen_values)
    if r % 10_000 == 0:
        print (r)


plt.hist(eigenvalues, bins=200, density=True)
plt.savefig(betas[beta] + " eigenvalues")
plt.show()
