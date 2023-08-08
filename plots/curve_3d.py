import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt


def demo():
    mpl.rcParams['legend.fontsize'] = 10

    fig = plt.figure(dpi=160)
    ax = fig.add_subplot(projection='3d')

    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-4, 4, 100) / 4
    r = z**3 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)

    ax.plot(x, y, z, label='parametric curve')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.legend()
    plt.tight_layout()
    # plt.show()
    plt.savefig('./figures/3D_curve_demo.png')
    return None


if __name__ == '__main__':
    demo()
