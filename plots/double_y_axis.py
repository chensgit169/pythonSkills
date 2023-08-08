import matplotlib.pyplot as plt
import numpy as np

color_list = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

z = np.arange(0, 10, 1)
r = z**2
b = np.exp(-z**2)

fig = plt.figure(dpi=160)
ax = fig.add_subplot(1, 1, 1)

h1, = ax.plot(z, z, color=color_list[0])
ax.set_title("Electron Trajectory and Magnetic Field on Axis")
ax.set_xlabel('z')
ax.set_ylabel('r/mm')

ax2 = ax.twinx()
h2, = ax2.plot(z, b, '-', color=color_list[1], linewidth=2)
ax2.set_ylabel('$B_z(z,r=0)$ / T')


ax2.spines['left'].set_color(color_list[0])
ax2.spines['right'].set_color(color_list[1])
ax.tick_params(axis='y', colors=color_list[0])
ax2.tick_params(axis='y', colors=color_list[1])
ax.yaxis.label.set_color(color_list[0])
ax2.yaxis.label.set_color(color_list[1])

# ax.legend([h1, h2], ['Trajectory', 'Field Distribution'])
plt.tight_layout()
# plt.show()
plt.savefig('./figures/double_yaxis.png', bbox_inches="tight")
