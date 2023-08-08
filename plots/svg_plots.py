import matplotlib.pyplot as plt
import matplotlib as mpl

# 生成数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 创建坐标轴对象
fig, ax = plt.subplots()

# 绘制折线图
ax.plot(x, y)

# 设置坐标轴标签
ax.set_xlabel('X轴标签')
ax.set_ylabel('Y轴标签')

# 设置图标题
ax.set_title('折线图示例')

# 显示网格
ax.grid(False)

# 将坐标轴背景绘制为透明
mpl.rcParams['patch.facecolor'] = 'none'
plt.savefig('line_chart.png', format='png')

# 显示图形
plt.show()
