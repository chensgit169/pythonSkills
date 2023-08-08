from compiler.qasm.qasm import Qasm

file_path = 'examples/simple.qasm'

with open(file_path, 'r') as qfile:
    data = qfile.read()

qasm = Qasm(data=data)
print(type(qasm.parse()))
