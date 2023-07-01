from find_roots import find_roots_in_interval
import math


def check(func, edge_lengths_sum, method):
    interval_size = 4000
    roots1 = find_roots_in_interval(func, interval_size, 600, method=method)
    roots2 = find_roots_in_interval(func, interval_size * 2, 600, method=method)
    roots3 = find_roots_in_interval(func, interval_size * 3, 600, method)
    roots4 = find_roots_in_interval(func, interval_size * 4, 600, method)
    # roots5 = find_roots_in_interval(func, interval_size * 5, 300)

    counts = [len(roots1), len(roots2), len(roots3), len(roots4)]# len(roots5)]

    print(f"{counts}")
    diffs = []
    i = 0
    for count in counts:
        x = (edge_lengths_sum / math.pi) * (interval_size + interval_size * i)
        diffs.append(x - count)
        i = i + 1

    print(diffs)
