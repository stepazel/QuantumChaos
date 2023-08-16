import numpy as np
import matplotlib.pyplot as plt

roots = np.load('5complete_graph_roots2000.npy')

plt.hist(roots, 100)
plt.show()
