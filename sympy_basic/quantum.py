from sympy.physics.quantum.gate import CNOT, H
from sympy.physics.quantum import Ket, Bra, density, qubit
from sympy.abc import lamda
from circuitplot import CircuitPlot, labeller, Mz

from sympy.physics.paulialgebra import Pauli, evaluate_pauli_product
from sympy import I

import matplotlib.pyplot as plt
from sympy import latex
#
circuits = Mz(0) * CNOT(0, 1) * H(0)
# # with plt.xkcd():
circuit_plot = CircuitPlot(circuits, 2)
circuit_plot.set_labels(labeller(2, 'q'))
circuit_plot.plot()
plt.tight_layout()
# plt.savefig('./basic.svg', format='svg')

plt.show()
# k = Ket('psi') * Bra('psi')
# print()
#
# with open('state.md', 'w') as f:
#     f.write('$$\n')
#     f.write(latex(k) + '\n')
#     f.write(latex(Pauli(1)) + '\n')
#     f.write('\n$$')


