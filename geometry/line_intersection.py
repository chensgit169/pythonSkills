import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

In = np.loadtxt('data/in.txt', dtype=int)
Jn = np.loadtxt('data/Jn.txt', dtype=int)

rr = np.loadtxt('data/rr.txt')
zz = np.loadtxt('data/zz.txt')

mag_zone = np.loadtxt('data/mag_zone.txt', dtype=int)
edges = [{'j': array[:2], 'i': array[2:4]} for array in mag_zone]
pprint(edges)


class Line:
    def __init__(self, n, points, line_type: str):
        self.n = n
        self.points = points
        self.  line_type = line_type

        self.point_lookup = {tuple(p): i for i, p in enumerate(points.T)}

    def __repr__(self):
        return self.line_type + str(self.n)

    def intersect(self, other: 'Line'):
        nodes0 = {tuple(p) for p in self.points.T}
        nodes1 = {tuple(p) for p in other.points.T}

        intersect_points = set.intersection(nodes0, {tuple(p) for p in nodes1})
        print(intersect_points)
        if intersect_points is {}:
            return None
        elif len(intersect_points) == 1:
            point = intersect_points.pop()
            n0 = self.point_lookup[point]
            n1 = other.point_lookup[point]
            return n0, n1
        else:
            raise Exception


def encode_lines():
    lines = {}

    for i in range(zz.shape[0]):
        zs = zz[i, :]
        rs = rr[i, :]
        line = Line(In[i], np.array([zs, rs]), 'i')
        lines[repr(line)] = line

    for j in range(zz.shape[1]):
        zs = zz[:, j]
        rs = rr[:, j]
        line = Line(Jn[j], np.array([zs, rs]), 'j')
        lines[repr(line)] = line

    return lines


class Block:
    def __init__(self, lines, edge_pair):
        i0 = 'i' + str(edge_pair['i'][0])
        i1 = 'i' + str(edge_pair['i'][1])
        j0 = 'j' + str(edge_pair['j'][0])
        j1 = 'j' + str(edge_pair['j'][1])


def view():
    lines = encode_lines()
    for _, line in lines.items():
        zs, rs = line.points
        plt.plot(zs, rs, '--')

    for pairs in edges[:1]:
        edge_lines = [lines['i' + str(n)] for n in pairs['i']] + \
                     [lines['j' + str(n)] for n in pairs['j']]
        for line in edge_lines:
            zs, rs = line.points
            plt.plot(zs, rs, '-*', color='black')
    plt.show()


def test():
    lines = encode_lines()
    line0 = lines['i2']
    line1 = lines['j2']
    n0, n1 = line0.intersect(line1)
    print(n0, n1)
    print(In[n0], Jn[n1])


view()
