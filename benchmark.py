from find_roots import find_roots_in_interval
from numpy import sin
from dirichlet_standard.equations import dirichlet_standard
from dirichlet.roots import func

print(len(find_roots_in_interval(func, 100_000, 400, 'bisect')))
print(len(find_roots_in_interval(func, 100_000, 400, 'brentq')))