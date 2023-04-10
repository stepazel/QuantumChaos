import numpy as np
import matplotlib.pyplot as plt
from plots import gue

# Change all GUE values to anything else

roots = np.load('GUE 1000x1000.npy')
len(roots)
plt.hist(roots, bins=200, density=True)
x = np.arange(0, 5, 0.05)

plt.plot(x, gue(x), label='GUE')
plt.legend()
plt.xlabel('Normalized spacings of eigenvalues')
plt.ylabel('Frequency')
plt.xlim(xmin=0, xmax=5)
plt.title('Histogram for GUE matrix n=1000')
plt.savefig('gue')
