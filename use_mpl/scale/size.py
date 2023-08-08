import matplotlib.pyplot as plt

fig, ax = plt.subplots()
print(fig.get_size_inches())  # [6.4, 4.8]
print(fig.get_dpi())  # 100.0

# set margins of the figure
plt.subplots_adjust(left=0.125, right=0.9, bottom=0.125, top=0.9)

ax.set_aspect(1.0)
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.plot([0, 0, 8, 8, 4],
        [0, 6, 0, 6, 3], '*')
plt.title('Plotting: "*"', fontsize=20)

# 打印默认边距
print(fig.subplotpars.left)    # 输出: 0.125
print(fig.subplotpars.right)   # 输出: 0.9
print(fig.subplotpars.bottom)  # 输出: 0.125
print(fig.subplotpars.top)     # 输出: 0.9
plt.show()
