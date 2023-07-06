import sympy as sp
from sympy import cos, sin
from numpy import pi, e, sqrt

k, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10 = sp.symbols('k l1 l2 l3 l4 l5 l6 l7 l8 l9 l10', real=True)

# TODO zkusit jine delky hran.. preci e^3 by tam asi nemelo byt

edge_lengths = [pi, e, sqrt(2), sqrt(3), sqrt(e), 1.2654, 0.5, sqrt(sqrt(2)), pi ** 2, e ** 3]

matrix = sp.Matrix([
    # A
    [1, 0, 0, 0, 0, 0, 0, 0, -cos(l5*k), -sin(l5*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -cos(l9*k), -sin(l9*k), 0, 0,],
    [0, k, 0, 0, 0, 0, 0, 0, k*sin(l5*k), -k*cos(l5*k), 0, k, 0, 0, 0, 0, k*sin(l9*k), -k*cos(l9*k), 0, 0],
    # B
    [cos(l1*k), sin(l1*k), -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [cos(l1*k), sin(l1*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
    [cos(l1*k), sin(l1*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -cos(l10*k), -sin(l10*k)],
    [k*sin(l1*k), -k*cos(l1*k), 0, k, 0, 0, 0, 0, 0, 0, 0, 0, 0, k, 0, 0, 0, 0, k*sin(l10*k), -k*cos(l10*k)],
    # C 
    [0, 0, cos(l2*k), sin(l2*k), -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, cos(l2*k), sin(l2*k), 0, 0, 0, 0, 0, 0, -cos(l6*k), -sin(l6*k), 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, cos(l2*k), sin(l2*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0,],
    [0, 0, k*sin(l2*k), -k*cos(l2*k), 0, k, 0, 0, 0, 0, k*sin(l6*k), -k*cos(l6*k), 0, 0, 0, k, 0, 0, 0, 0,],
    # D
    [0, 0, 0, 0, cos(l3*k), sin(l3*k), -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, cos(l3*k), sin(l3*k), 0, 0, 0, 0, 0, 0, -cos(l7*k), -sin(l7*k), 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, cos(l3*k), sin(l3*k), -0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0,],
    [0, 0, 0, 0, k*sin(l3*k), -k*cos(l3*k), 0, k, 0, 0, 0, 0, 0, 0, k*sin(l7*k), -k*cos(l7*k), 0, 0, 1, 0,],
    # E
    [0, 0, 0, 0, 0, 0, cos(l4*k), sin(l4*k), -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, cos(l4*k), sin(l4*k), 0, 0, 0, 0, 0, 0, -cos(l8*k), -sin(l8*k), 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, cos(l4*k), sin(l4*k), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
    [0, 0, 0, 0, 0, 0, k*sin(l4*k), -k*cos(l4*k), 0, k, 0, 0, 0, 0, k*sin(l8*k), -k*cos(l8*k), 0, 0, 0, k]
    ])




