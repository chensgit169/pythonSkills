import matplotlib.pyplot as plt
import numpy as np


def bloch_sphere(theta, phi):
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return x, y, z


theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

x, y, z = bloch_sphere(theta, phi)
dist_to_center = np.sqrt(x ** 2 + y ** 2 + z ** 2)  # 计算每个点到中心的距离

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制热图
scatter = ax.scatter(x, y, z, c=dist_to_center, cmap='hot', alpha=0.5)

ax.plot_surface(x, y, z, color='#ADD8E6',
                alpha=0.2, edgecolor='black')

# 添加坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 设置坐标轴刻度范围
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

# 设置XYZ比例
ax.set_box_aspect([1, 1, 1])

# 添加颜色条
cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('Distance to Center')

# 隐藏坐标轴刻度
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# 隐藏坐标轴
ax.axis('off')

plt.show()
