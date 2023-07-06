import math
from find_roots import find_roots
from equations import dirichlet_standard, edge_lengths
from numpy import save

edge_lengths_sum = sum(edge_lengths)


def func(x):
    return dirichlet_standard(x, edge_lengths)


number_of_roots = 100_000
roots = find_roots(func, number_of_roots)
save(f"dirichlet_standard_roots_{number_of_roots}", roots)
