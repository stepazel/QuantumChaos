from weyl_law_check import check
from roots import func
from matrix import edge_lengths2

check(func, sum(edge_lengths2), interval_size=20)