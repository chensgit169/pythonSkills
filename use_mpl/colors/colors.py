import matplotlib.pyplot as plt
import numpy as np


BLUE = '#1f77b4'
ORANGE = '#ff7f0e'
GREEN = '#2ca02c'
RED = '#d62728'
PURPLE = '#9467bd'
BROWN = '#8c564b'
PINK = '#e377c2'
GRAY = '#7f7f7f'
YELLOW = '#bcbd22'
CYAN = '#17becf'
color_list = [BLUE, ORANGE, GREEN, RED, PURPLE, BROWN, PINK, GRAY, YELLOW, CYAN]


plt.figure(dpi=160)
plt.title('Default Colors of plt')
for i, color in enumerate(color_list):
    plt.plot([i, i+0.5], [i, i+0.5], color=color, label=color)
    plt.text(i, i+0.5, str(i))
plt.legend()
plt.savefig('./figures/default_colors.png')
