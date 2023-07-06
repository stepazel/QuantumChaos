from dirichlet_standard.equations import dirichlet_standard, edge_lengths
from weyl_law_check import check


def func(x):
    return dirichlet_standard(x, edge_lengths)


if __name__ == '__main__':
    edge_lengths_sum = sum(edge_lengths)
    check(func, edge_lengths_sum)
