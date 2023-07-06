import math


# edge_lengths = [math.pi, math.e, math.sqrt(2), math.sqrt(3), math.sqrt(math.e), 1.2654]
edge_lengths = [math.pi, math.e, math.sqrt(2), math.sqrt(3), math.sqrt(math.e), math.pi**3]


def dirichlet_standard(k: float, a: list) -> object:
    cos = math.cos
    sin = math.sin
    return cos(a[0] * k) * sin(a[1] * k) * sin(a[2] * k) * sin(a[3] * k) * sin(a[4] * k) * sin(a[5] * k) \
           + cos(a[1] * k) * sin(a[2] * k) * sin(a[3] * k) * sin(a[4] * k) * sin(a[5] * k) * sin(a[0] * k) \
           + cos(a[2] * k) * sin(a[3] * k) * sin(a[4] * k) * sin(a[5] * k) * sin(a[0] * k) * sin(a[1] * k) \
           + cos(a[3] * k) * sin(a[4] * k) * sin(a[5] * k) * sin(a[0] * k) * sin(a[1] * k) * sin(a[2] * k) \
           + cos(a[4] * k) * sin(a[5] * k) * sin(a[0] * k) * sin(a[1] * k) * sin(a[2] * k) * sin(a[3] * k) \
           + cos(a[5] * k) * sin(a[0] * k) * sin(a[1] * k) * sin(a[2] * k) * sin(a[3] * k) * sin(a[4] * k)
