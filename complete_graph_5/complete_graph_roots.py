from sympy.parsing.mathematica import parse_mathematica
import sympy
from sympy import lambdify
import numpy as np
from find_roots import find_roots

with open('det.txt', 'r') as file:
    content = file.read()

# ending interval 6762.495 for 100_000 roots!!
# weyl's law : 93775 for this interval

expr_str = parse_mathematica(content)

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

if __name__ == '__main__':
    # with ProcessPoolExecutor(12) as exe:
    roots = find_roots(func, 100000, 200)
    np.save(f"5complete_graph_roots{100000}a", roots)



