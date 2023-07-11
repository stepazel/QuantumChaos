import sympy as sp
from sympy import cos, sin
from numpy import pi, e, sqrt, log

k, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15 = sp.symbols('k l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 l12 l13 l14 l15', real=True)

edge_lengths = [pi, e, sqrt(2), log(2), 1.98712, sqrt(5), sqrt(e), log(5), sqrt(pi), log(7), sqrt(3), log(3), log(pi), sqrt(7), 2.3128628]
# TODO zkontrolovat (rucne a pomoci chat GPT)
matrix = sp.Matrix([
    # A
    [cos(l1*k), sin(l1*k), 0, 0, 0, 0, 0, 0, 0, 0, -cos(l6*k), -sin(l6*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [cos(l1*k), sin(l1*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [cos(l1*k), sin(l1*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -cos(l11*k), -sin(l11*k), 0, 0, 0, 0, 0, 0, 0, 0],
    [cos(l1*k), sin(l1*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, k, 0, 0, 0, 0, 0, 0, 0, 0, k*sin(l6*k), -k*cos(l6*k), 0, k, 0, 0, 0, 0, 0, 0, k*sin(l11*k), k*cos(l11*k), 0, 0, 0, k, 0, 0, 0, 0],
    # B
    [cos(l1*k), sin(l1*k), -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [cos(l1*k), sin(l1*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [cos(l1*k), sin(l1*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -cos(l12*k), -sin(l12*k), 0, 0, 0, 0, 0, 0],
    [cos(l1*k), sin(l1*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
    [k*sin(l1*k), -k*cos(l1*k), 0, k, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, k, 0, 0, 0, 0, 0, 0, k*sin(l12*k), -k*cos(l12*k), 0, 0, 0, k, 0, 0],
    # C
    [0, 0, cos(l2*k), sin(l2*k,), -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, cos(l2*k), sin(l2*k,), 0, 0, 0, 0, 0, 0, 0, 0, -cos(l7*k), -sin(l7*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, cos(l2*k), sin(l2*k,), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, cos(l2*k), sin(l2*k,), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
    [0, 0, k*sin(l2*k), -k*cos(l2*k), 0, k, 0, 0, 0, 0, 0, 0, k*sin(l7*k), -k*cos(l7*k), 0, 0, 0, k, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, k],
    # D
    [0, 0, 0, 0, cos(l3*k), sin(l3*k), -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, cos(l3*k), sin(l3*k), 0, 0, 0, 0, 0, 0, 0, 0, -cos(l8*k), -sin(l8*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, cos(l3*k), sin(l3*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, cos(l3*k), sin(l3*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -cos(l13*k), -sin(l13*k), 0, 0, 0, 0],
    [0, 0, 0, 0, k*sin(l3*k), -k*cos(l3*k), 0, k, 0, 0, 0, 0, 0, 0, k*sin(l8*k), -k*cos(l8*k), 0, 0, 0, k, 0, 0, 0, 0, k*sin(l13*k), -k*cos(l13*k), 0, 0, 0, 0],
    # E
    [0, 0, 0, 0, 0, 0, cos(l4*k), sin(l4*k), -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, cos(l4*k), sin(l4*k), -0, 0, 0, 0, 0, 0, 0, 0, -cos(l9*k), -sin(l9*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, cos(l4*k), sin(l4*k), -0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, cos(l4*k), sin(l4*k), -0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -cos(l14*k), -sin(l14*k), 0, 0],
    [0, 0, 0, 0, 0, 0, k*sin(l4*k), -k*cos(l4*k), 0, k, 0, 0, 0, 0, 0, 0, k*sin(l9*k), -k*cos(l9*k), 0, 0, 0, k, 0, 0, 0, 0, k*sin(l14*k), -k*cos(l14*k), 0, 0],
    # F
    [0, 0, 0, 0, 0, 0, 0, 0, cos(l5*k), sin(l5*k), -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, cos(l5*k), sin(l5*k), 0, 0, 0, 0, 0, 0, 0, 0, -cos(l10*k), -sin(l10*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, cos(l5*k), sin(l5*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, cos(l5*k), sin(l5*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -cos(l15*k), sin(l15*k)],
    [0, 0, 0, 0, 0, 0, 0, 0, k*sin(l5*k), -k*cos(l5*k), 0, k, 0, 0, 0, 0, 0, 0, k*sin(l10*k), -k*cos(l10*k), 0, 0, 0, 0, 0, 0, 0, 0, k*sin(l15*k), -k*cos(l15*k)]
    ])




