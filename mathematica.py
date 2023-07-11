from sympy import Matrix
from sympy.parsing.mathematica import parse_mathematica
from sympy import lambdify
from sympy import sympify
from sympy import Symbol
from numpy import pi, e


def convert_to_mathematica_matrix(matrix: Matrix) -> str:
    """ Converts sympy matrix into a string that can be pasted into Mathematica input. """
    matrix_str = str(matrix.tolist())
    return matrix_str \
        .replace('[', '{')\
        .replace(']', '}')\
        .replace('cos', 'Cos')\
        .replace('sin', 'Sin')\
        .replace('(', '[')\
        .replace(')', ']')


def get_func_from_mathematica(file_name: str):
    with open(file_name, 'r') as file:
        content = file.read()

    expr_str = parse_mathematica(content)

    # Convert the string to a sympy expression
    expr = sympify(expr_str)

    # Define the variables
    k = Symbol('k')
    # pi = Symbol('pi')
    # e = Symbol('e')
    # Use lambdify to create a function that can be evaluated numerically
    subbed_expr = expr.subs({'pi': pi, 'e': e})
    func = lambdify(k, subbed_expr, 'numpy')
    return func

