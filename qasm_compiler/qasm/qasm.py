# This code is part of Qiskit.
#
# (C) Copyright IBM 2017.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
OPENQASM circuit object.
"""
from .qasmparser import QasmParser


class Qasm:
    """OPENQASM circuit object."""

    def __init__(self, data=None):
        self._data = data

    def parse(self):
        """Parse the data."""

        with QasmParser() as qasm_p:
            return qasm_p.parse(self._data)
