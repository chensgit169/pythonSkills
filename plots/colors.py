import matplotlib.pyplot as plt
import numpy as np


color_list = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

plt.figure(dpi=160)
plt.title('Default Colors of plt')
for i, color in enumerate(color_list):
    plt.plot([i, i+0.5], [i, i+0.5], color=color, label=color)
    plt.text(i, i+0.5, str(i))
plt.legend()
plt.savefig('./figures/default_colors.png')
