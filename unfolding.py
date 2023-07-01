from sympy import symbols, integrate, sqrt, pi
import numpy as np
from skrmt.ensemble import GaussianEnsemble


t = symbols("t")
N, β = symbols("N β", positive=True)
σ = 2/(pi*(2*β*N)) * sqrt((2*β*N) - t**2)
Λ_N_β = integrate(N*σ, t)

λ = symbols("λ")
F_λ = Λ_N_β.subs(t, λ) - Λ_N_β.subs(t, -sqrt(2*β*N))


def F(eig, size, beta):
    if eig <= -np.sqrt(2*beta*size):
        return 0
    if eig >= np.sqrt(2*beta*size):
        return size
    else:
        # F_λ is defined outside this function
        return float(F_λ.subs(β, beta).subs(N, size).subs(λ, eig).evalf())


# matrix_size = 300
# A = GaussianEnsemble(beta=1, n=matrix_size).matrix
# λs, V = np.linalg.eigh(A)
# λ_bar = [F(eigenvalue, matrix_size, 1) for eigenvalue in λs]
# eig_spaces = [λ_bar[i+1] - λ_bar[i] for i in range(matrix_size-1)]
# print(np.mean(np.diff(λs)))





