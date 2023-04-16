from dirichlet_standard.equations import dirichlet_standard
from weyl_law_check import check
import math


def func(x):
    return dirichlet_standard(x, edge_lengths)


if __name__ == '__main__':
    edge_lengths = [math.pi, math.e, math.sqrt(2), math.sqrt(3), math.sqrt(math.e), 1.2654]
    edge_lengths_sum = sum(edge_lengths)
    check(func, edge_lengths_sum)
