import math
from roots import find_roots
from equations import dirichlet_standard
from numpy import save

edge_lengths = [math.pi, math.e, math.sqrt( 2), math.sqrt(3), math.sqrt(math.e), 1.2654]
edge_lengths_sum = sum(edge_lengths)


def func(x):
    return dirichlet_standard(x, edge_lengths)


number_of_roots = 10_000_000
roots = find_roots(func, number_of_roots)
save(f"dirichlet_standard_roots_{number_of_roots}", roots)
