import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bit_num = 136
height, width = 12, 12
data = pd.read_excel('./ScQ-P%d信息.xlsx' % bit_num)
connection = [tuple(_.split('_')) for _ in data['Connection']]
print(data['Qubit'])

qubits = data['Qubit'][:bit_num]
xy = [(int(_[3:]), int(_[1:3])) for _ in qubits]
# broken = [7, 18, 49, 55, 60, 78, 118, 131]
nodes = []
# for i in range(height*width):
#     x = i % width
#     y = i // width
#     if i in broken:
#         name = None
#     else:
#         name = next(qubits)
#     nodes.append([(x, y), name])

xy = np.array(xy).T
print(xy)
plt.gca().invert_yaxis()
plt.scatter(xy[0], xy[1])
plt.show()


class Qubit:
    def __init__(self, name: str):
        self.name = name
        self.linked = []

    def link(self, another):
        self.linked.append(another.name)

    @property
    def tensor(self):
        raise NotImplemented

    def absorb(self, another, axis):
        raise NotImplemented
