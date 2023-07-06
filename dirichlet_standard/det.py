from sympy import sin, cos, symbols, Matrix

k, l1, l2, l3, l4, l5, l6 = symbols('k l1 l2 l3 l4 l5 l6')

matrix = Matrix([
    [sin(k*l1), -sin(l2*k), 0, 0, 0, 0],
    [sin(l1*k), 0, -sin(l3*k), 0, 0, 0],
    [sin(l1*k), 0, 0, -sin(l4*k), 0, 0],
    [sin(l1*k), 0, 0, 0, -sin(l5*k), 0],
    [sin(l1*k), 0, 0, 0, 0, -sin(l6*k)],
    [cos(l1*k), cos(k*l2), cos(l3*k), cos(l4*k), cos(l5*k), cos(l6*k)],
])

det = matrix.det()

print(det)