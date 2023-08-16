import numpy as np
import matplotlib.pyplot as plt
from equations import dirichlet_standard, edge_lengths

# def func(h):
#     return dirichlet_standard(h, edge_lengths)

x = np.arange(0, 10, 0.01)
plt.plot(x, dirichlet_standard(x))
# roots = np.load('dirichlet_standard_roots_10000000.npy')
#

# plt.hist(roots, 200, density=False)
plt.show()