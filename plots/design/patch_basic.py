import numpy as np
from matplotlib import patches
import matplotlib.pyplot as plt

# 绘制一个椭圆需要制定椭圆的中心，椭圆的长和高
xcenter, ycenter = 1, 1
width, height = 0.8, 0.5
angle = -90  # 椭圆的旋转角度

# 第一步：创建绘图对象
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
ax.set_xbound(-1, 3)
ax.set_ybound(-1, 3)

e1 = patches.Ellipse((xcenter, ycenter), width, height,
                     angle=angle, linewidth=2, fill=False, zorder=2)

e2 = patches.Arc((xcenter, ycenter), width, height,
                 angle=angle, linewidth=2, theta1=0, theta2=180, fill=False, zorder=2)

ax.add_patch(e2)

# hide axis
plt.axis('off')

plt.show()
