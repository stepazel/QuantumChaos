from numpy import pi, e


def goe(x):
    return (pi / 2) * x * (e ** ((-pi / 4) * x ** 2))


def gue(x):
    return (32 / pi ** 2) * x ** 2 * (e ** ((-4 / pi) * x ** 2))


def gse(x):
    return ((2 ** 18) / (3 ** 6 * pi ** 3)) * x ** 4 * (
                e ** ((-64 / (9 * pi)) * x ** 2))


def poisson(x):
    return e ** (-x)


def normalize_root(root: float, edge_lengths_sum: float) -> float:
    return (root * edge_lengths_sum) / pi
