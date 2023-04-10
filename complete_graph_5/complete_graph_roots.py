from sympy.parsing.mathematica import parse_mathematica
from sympy import symbols
import sympy
from sympy import lambdify
import numpy as np
from find_roots import find_roots_in_interval, find_roots

with open('det.txt', 'r') as file:
    content = file.read()

expr_str = parse_mathematica(content)

# expr_str = "sin(sqrt(2)*k)*sin(e*k)**3*sin(pi*k)**7*sin(e**3*k)*cos(0.5*k)"

# Convert the string to a sympy expression
expr = sympy.sympify(expr_str)

# Define the variables
k = sympy.Symbol('k')
pi = sympy.Symbol('pi')
e = sympy.Symbol('e')
# Use lambdify to create a function that can be evaluated numerically
subbed_expr = expr.subs({'pi': np.pi, 'e': np.e})
func = lambdify(k, subbed_expr, 'numpy')

# Evaluate the function at a particular value of k and given values of E, pi, and e

# roots = find_roots_in_interval(func, 10, 100, 'brentq')
roots = find_roots(func, 100_000, 100)
np.save(f"5complete_graph_roots{100_000}", roots)

print(len(roots))



