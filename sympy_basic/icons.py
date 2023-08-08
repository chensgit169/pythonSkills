import matplotlib.pyplot as plt
import numpy as np
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection


# 定义函数，给每一个patch都设置标签说明
def label(xy, text):
    y = xy[1] - 0.15  # 标签放置在patch下方的0.15位置处
    plt.text(xy[0], y, text, ha="center", family='sans-serif', size=14)


fig, ax = plt.subplots()

# 3j, 3j means 3 by 3, closed at both ends
grid = np.mgrid[0.2:0.8:3j, 0.2:0.8:3j].reshape(2, -1).T

patches = []

circle = mpatches.Circle(xy=grid[0], radius=0.1, ec="none")
patches.append(circle)
label(grid[0], "Circle")

# 添加一个Rectangle
rect = mpatches.Rectangle(grid[1] - [0.025, 0.05], 0.05, 0.1, ec="none")
patches.append(rect)
label(grid[1], "Rectangle")

# 添加一个楔形，即圆的一部分
wedge = mpatches.Wedge(grid[2], 0.1, 30, 270, ec="none")
patches.append(wedge)
label(grid[2], "Wedge")

# 添加一多边形，这里添加一个五边形
polygon = mpatches.RegularPolygon(grid[3], numVertices=5, radius=0.1)
patches.append(polygon)
label(grid[3], "Polygon")

# 添加一个椭圆，也可以使用Arc
ellipse = mpatches.Ellipse(grid[4], 0.2, 0.1)
patches.append(ellipse)
label(grid[4], "Ellipse")

# 添加一个箭头
arrow = mpatches.Arrow(grid[5, 0] - 0.05, grid[5, 1] - 0.05, 0.1, 0.1,
                       width=0.1)
patches.append(arrow)
label(grid[5], "Arrow")

# 添加一个路径path，路径的详细解释后面会讲到，相比于简单的patch，稍显复杂
Path = mpath.Path
path_data = [
    (Path.MOVETO, [0.018, -0.11]),
    (Path.CURVE4, [-0.031, -0.051]),
    (Path.CURVE4, [-0.115, 0.073]),
    (Path.CURVE4, [-0.03, 0.073]),
    (Path.LINETO, [-0.011, 0.039]),
    (Path.CURVE4, [0.043, 0.121]),
    (Path.CURVE4, [0.075, -0.005]),
    (Path.CURVE4, [0.035, -0.027]),
    (Path.CLOSEPOLY, [0.018, -0.11])]
codes, verts = zip(*path_data)
path = mpath.Path(verts + grid[6], codes)
patch = mpatches.PathPatch(path)
patches.append(patch)
label(grid[6], "PathPatch")

# 添加一个box
fancybox = mpatches.FancyBboxPatch(
    grid[7] - [0.025, 0.05], 0.05, 0.1,
    boxstyle=mpatches.BoxStyle("Round", pad=0.02))
patches.append(fancybox)
label(grid[7], "FancyBboxPatch")

# 添加一条折线——注意这里的折线和前面所画的这显示不一样的，这里的折线是一个形状
x, y = np.array([[-0.06, 0.0, 0.1], [0.05, -0.05, 0.05]])
line = mlines.Line2D(x + grid[8, 0], y + grid[8, 1], lw=5., alpha=0.3)
label(grid[8], "Line2D")

colors = np.linspace(0, 1, len(patches))

# 将patch集合包装成PatchCollection
collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=0.3)
collection.set_array(np.array(colors))

# 将PatchCollection添加给axes对象
ax.add_collection(collection)

# 将折线添加到axes对象
ax.add_line(line)
plt.axis('equal')
# plt.axis('off')
plt.tight_layout()
plt.grid()
plt.show()
