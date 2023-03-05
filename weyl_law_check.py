from equations import dirichlet_standard
from roots import find_roots_in_interval
from numpy import diff
import math

edge_lengths = [math.pi, math.e, math.sqrt(2), math.sqrt(3), math.sqrt(math.e), 1.2654]
edge_lengths_sum = sum(edge_lengths)

def func(x):
    return dirichlet_standard(x, edge_lengths)

roots1 = find_roots_in_interval(func, 12_000, 400)
roots2 = find_roots_in_interval(func, 16_000, 400)
roots3 = find_roots_in_interval(func, 20_000, 400)
roots4 = find_roots_in_interval(func, 24_000, 400)
roots5 = find_roots_in_interval(func, 28_000, 400)

counts = [len(roots1), len(roots2), len(roots3), len(roots4), len(roots5)]

print(f"{counts}")
diffs = []
i = 1
for count in counts:
    x = (edge_lengths_sum/math.pi) * (8000 + 4_000 * i)
    diffs.append(x - count)
    i = i + 1

print(diffs)

