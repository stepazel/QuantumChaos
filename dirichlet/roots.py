from find_roots import find_roots
import numpy as np
from numpy import sin

# edges
# e = [np.pi, np.e, np.sqrt(2), np.pi ** 2, 1.486, np.sqrt(np.e)]


# 2
# e = [np.pi, np.e, np.sqrt(2), np.log(2), 0.5772156649, np.sqrt(3)]
# 4
# e = [np.pi, np.e, np.sqrt(2), np.log(2), 1.61, np.sqrt(3)]
# 5
# e = [np.pi, np.e, np.sqrt(2), np.log(2), np.e**2, np.sqrt(3)]
# 6
# e = [np.pi, np.e, np.sqrt(2), np.log(2), 1.61, np.sqrt(5)]
# 7
# e = [np.pi, np.e, np.sqrt(2), np.log(2), 1.98712, np.sqrt(5)]
# 8

# In these lengths, one length is drsctically larger than the others)
# eLarge = [np.pi, np.e, np.sqrt(2), np.log(2), 1.98712, np.sqrt(5), np.sqrt(np.e), np.log(5), np.sqrt(np.pi), 0.97127, np.sqrt(3), np.log(3), np.exp(np.pi)]
# e3 = [np.pi, np.e, np.sqrt(2), np.log(2), 1.98712, np.sqrt(5), np.sqrt(np.e), np.log(5), np.sqrt(np.pi), 0.97127, np.sqrt(3), np.log(3), np.log(np.pi)]
# e = [np.pi, np.e, np.sqrt(2), np.log(2), 1.98712, np.sqrt(5), np.sqrt(np.e), np.log(5), np.sqrt(np.pi), 0.97127, np.sqrt(3), np.log(3), np.log(np.pi), 1.52321, 0.86127]
# e = [np.pi, np.e, np.sqrt(5), 2.5]# np.log(5), np.sqrt(np.pi)]
# e = [np.pi, np.e, np.sqrt(5), 2.5, np.log(5), np.pi**3]
e = [np.pi, np.e, np.sqrt(5), np.pi**3, np.log(5), np.pi**3]
# e = [1, 2, 3, 4, 5, 6]

# TODO dirichlet - zkusit vice hran (vice sinu), ty delky at jsou vicemene stejne a zkusit vice setu hran a ty zprumerovat, zaroven je mozne, ze ta presnost je mala?
#  Zkontrolovat to rucne s Desmosem!! Pak zkontrolovat weylovu asymptotiku
#  complete graph - hele zkusit ty hrany taky nejak podobne + weylova asymptotika

def func(k: float) -> float:
    return sin(e[0] * k) \
           * sin(e[1] * k) \
           * sin(e[2] * k) \
           * sin(e[3] * k) \
           # * sin(e[4] * k) \
           # * sin(e[5] * k) \
           # * sin(e[6] * k) \
           # * sin(e[7] * k) \
           # * sin(e[8] * k) \
           # * sin(e[9] * k) \
           # * sin(e[10] * k) \
           # * sin(e[11] * k) \
           # * sin(e[12] * k) \
           # * sin(e[13] * k) \
           # * sin(e[14] * k) \


if __name__ == '__main__':
    roots = find_roots(func, 100_000)
    np.save(f'roots3', roots)
