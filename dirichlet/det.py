from sympy import sin, symbols, Matrix

k, l1, l2, l3, l4, l5, l6 = symbols('k l1 l2 l3 l4 l5 l6')

matrix = Matrix([
    [sin(l1*k), 0, 0, 0, 0, 0],
    [0, sin(l2*k), 0, 0, 0, 0],
    [0, 0, sin(l3*k), 0, 0, 0],
    [0, 0, 0, sin(l4*k), 0, 0],
    [0, 0, 0, 0, sin(l5*k), 0],
    [0, 0, 0, 0, 0, sin(l6*k)],
])

det = matrix.det()

print(det)