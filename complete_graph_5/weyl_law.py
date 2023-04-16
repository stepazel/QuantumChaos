from weyl_law_check import check
from complete_graph_roots import func
from complete_graph_matrix import edge_lengths

check(func, sum(edge_lengths))