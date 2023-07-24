from shapely.geometry import Point, LineString, Polygon
import matplotlib.pyplot as plt

# 创建点
point = Point(2, 3)

# 创建线
line = LineString([(1, 1), (3, 5)])

# 创建多边形
polygon = Polygon([(1, 2), (4, 2), (3, 4), (2, 5)])

# 绘制几何对象
fig, ax = plt.subplots()
ax.set_aspect('equal')

# 绘制点
ax.plot(point.x, point.y, 'ro')

# 绘制线
ax.plot(*line.xy, 'b-')

# 绘制多边形
patch = plt.Polygon(list(polygon.exterior.coords), edgecolor='g', facecolor='none')
ax.add_patch(patch)

plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
