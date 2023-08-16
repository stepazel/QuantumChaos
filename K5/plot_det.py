from mathematica import get_func_from_mathematica
import matplotlib.pyplot as plt
import numpy as np

func = get_func_from_mathematica('det_k5.txt')
x = np.arange(0, 5, 0.01)

plt.plot(x, func(x))
plt.show()
