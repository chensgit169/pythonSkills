import numpy as np
import matplotlib.pyplot as plt

# 创建一个网格点坐标矩阵
x = np.linspace(-5, 5, 10)
y = np.linspace(-5, 5, 10)
X, Y = np.meshgrid(x, y)

# 绘制2D图像
fig = plt.figure()
ax = fig.add_subplot(aspect='equal')
ax.plot(X, Y, '*')

# 显示图像
plt.show()
