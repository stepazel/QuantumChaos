import numpy as np
import matplotlib.pyplot as plt
from plots import gue, goe, gse

# Change all GUE values to anything else

roots = np.load('../GSE50x50 unfolded and normalized.npy')
len(roots)
plt.hist(roots, bins=80, density=True)
x = np.arange(0, 5, 0.05)

plt.plot(x, gse(x), label='GSE')
plt.legend()
plt.xlabel('Normalized spacings of eigenvalues')
plt.ylabel('Frequency')
plt.xlim(xmin=0, xmax=5)
plt.title('Histogram for GSE matrix n=1000')
plt.savefig('gseee')
