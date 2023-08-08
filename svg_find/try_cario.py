import matplotlib.pyplot as plt

# 绘制量子线路图
with plt.xkcd():
    fig, ax = plt.subplots()
    ax.plot([0, 1], [1, 1], linewidth=2, color='gray', transparent=True)  # 绘制第一个量子比特的线路
    ax.plot([0, 1], [0, 0], linewidth=2, color='gray')  # 绘制第二个量子比特的线路
    ax.plot([0.5, 0.5], [0, 1], linewidth=2, color='gray')  # 绘制控制门线路
    ax.plot([0.5, 0.5], [0.8, 1.2], linewidth=2, color='black')  # 绘制控制门符号
    ax.plot([1.2, 1.2], [0.6, 1.4], linewidth=2, color='black')  # 绘制目标门符号
    ax.plot([1, 1.2], [1, 0.8], linewidth=2, color='blue')  # 绘制目标门连接线
    ax.plot([1, 1.2], [0, 0.6], linewidth=2, color='blue')  # 绘制目标门连接线

# 设置坐标轴范围
# ax.set_xlim([0, 1.5])
# ax.set_ylim([-0.5, 1.5])

# 设置坐标轴标签
# ax.set_xlabel('Circuit', fontsize=12)
# ax.set_ylabel('Qubit', fontsize=12)
# ax.set_title('Quantum Circuit Diagram', fontsize=14)
    plt.axis('off')
    # 显示图形
    plt.savefig('./circuit.png')
