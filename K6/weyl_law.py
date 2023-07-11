from weyl_law_check import check
from roots import func
from matrix import edge_lengths

check(func, sum(edge_lengths), interval_size=100)