from shapely.geometry import Point, LineString, Polygon

# 创建点
point1 = Point(0, 0)
point2 = Point(3, 4)

# 创建线
line = LineString([(0, 0), (3, 4), (1, 2)])

# 创建多边形
polygon = Polygon([(0, 0), (4, 0), (4, 4), (0, 4)])

# 计算线的长度
line_length = line.length
print("Line Length:", line_length)

# 判断点是否在多边形内
print("Point1 in Polygon:", point1.within(polygon))
print("Point2 in Polygon:", point2.within(polygon))

