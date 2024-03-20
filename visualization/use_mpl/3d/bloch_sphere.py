import matplotlib.pyplot as plt
import numpy as np


def bloch_sphere(thetas, phis):
    xs = np.sin(thetas) * np.cos(phis)
    ys = np.sin(thetas) * np.sin(phis)
    zs = np.cos(thetas)
    return xs, ys, zs


theta = np.linspace(0, np.pi, 20)
phi = np.linspace(0, 2 * np.pi, 20)
theta, phi = np.meshgrid(theta, phi)

x, y, z = bloch_sphere(theta, phi)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d_plots')

ax.plot_surface(x, y, z, color='white', alpha=0.2, edgecolor='black')

# 添加坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

r = 1.2  # 方框半径
# 设置坐标轴刻度范围
ax.set_xlim(-r, r)
ax.set_ylim(-r, r)
ax.set_zlim(-r, r)

# 隐藏坐标轴刻度
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_zticks([])


ax.set_box_aspect([1, 1, 1])

# 添加方框
# x_box = np.array([-r, r, r, -r, -r, r, r, -r]).reshape((2, 4))
# y_box = np.array([-r, -r, r, r, -r, -r, r, r]).reshape((2, 4))
# z_box = np.array([-r, -r, -r, -r, r, r, r, r]).reshape((2, 4))
# ax.plot_wireframe(x_box, y_box, z_box, color='k', alpha=0.3)

# 隐藏坐标轴
# ax.axis('off')
ax.grid(False)
ax.set_title('Bloch Sphere')
# plt.tight_layout()
plt.savefig('figures/bloch_sphere.png', dpi=300)
plt.show()


