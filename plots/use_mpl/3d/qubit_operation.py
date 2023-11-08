import matplotlib.pyplot as plt
import numpy as np
import itertools


AsymTensor3 = np.array([(i - j) * (j - k) * (k - i)/2
                        for i, j, k in itertools.product(range(3), repeat=3)]
                       ).reshape((3, 3, 3))
I3 = np.eye(3)


def rep_mat_trans(alpha_vec, a_mat):
    a_conj = a_mat.conj()
    aa_dg = a_mat.T @ a_conj

    m1 = (aa_dg + aa_dg.T)
    m2 = (alpha_vec @ alpha_vec.conj() - np.trace(aa_dg)) * I3
    m3 = np.tensordot(AsymTensor3,
                      (alpha_vec @ a_conj - alpha_vec.conj() @ a_mat),
                      axes=([2], [0]))
    m_mat = m1 + m2 + 1j * m3
    c_vec = 2j * np.tensordot(AsymTensor3, aa_dg, axes=([0, 1], [0, 1]))
    return m_mat, c_vec


def operation(rs, alpha_vec, a_mat):
    # rs = np.array([xs, ys, zs]).T
    m_mat, c_vec = rep_mat_trans(alpha_vec, a_mat)

    # affine transformation
    rs_p = rs @ m_mat.T + c_vec
    xp, yp, zp = rs_p.T
    return xp, yp, zp


def demo(p: float):
    def bloch_sphere(thetas, phis):
        xs = np.sin(thetas) * np.cos(phis)
        ys = np.sin(thetas) * np.sin(phis)
        zs = np.cos(thetas)
        return xs, ys, zs

    theta = np.linspace(0, np.pi, 20)
    phi = np.linspace(0, 2 * np.pi, 20)
    theta, phi = np.meshgrid(theta, phi)

    x, y, z = bloch_sphere(theta, phi)
    rs = np.array([x, y, z]).T

    alpha_vec = np.array([np.sqrt(p), 0])
    a_mat = np.array([[0, 0, 0], [np.sqrt(1-p), 0, 0]])
    xp, yp, zp = operation(rs, alpha_vec, a_mat)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(xp, yp, zp, color='white', alpha=0.2, edgecolor='black')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    r = 1.2
    ax.set_xlim(-r, r)
    ax.set_ylim(-r, r)
    ax.set_zlim(-r, r)

    ax.set_box_aspect([1, 1, 1])

    ax.grid(False)
    # ax.set_title('Bloch Sphere')
    plt.savefig('figures/bit_flip.png', dpi=300)
    plt.show()


if __name__ == '__main__':
    demo(0.3)
