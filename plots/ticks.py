import matplotlib.pyplot as plt

# 生成示例数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 创建图像和坐标轴
fig, ax = plt.subplots()

# 绘制数据
ax.plot(x, y)

# 设置 x 轴标签旋转角度为 45 度
ax.set_xticks(x)
ax.set_xticklabels(['Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5'], rotation=45)

# 显示图像
plt.show()
