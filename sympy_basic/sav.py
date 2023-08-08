import sympy
import numpy as np

from sympy.abc import beta

from sympy import sqrt, sinh, cosh
from sympy import Array, zeros

ch = sqrt(cosh(beta))
sh = sqrt(sinh(beta))

# T = Array(2**6 * [0], shape=(2, 2, 2, 2, 2, 2))

T = Array([[ch, sh], [ch, sh], [ch, sh]])
T = T.reshape(3, 2, 1)
print(T)
