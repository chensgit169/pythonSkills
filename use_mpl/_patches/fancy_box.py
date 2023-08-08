import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe

# initialize a figure(canvas) and axes(container/subplot)
fig, ax = plt.subplots()
fig.set_size_inches(8, 6)

# settings of axes
# ax.set_aspect(1.0)
ax.set_xlim(-1, 10)
ax.set_ylim(-1, 10)
ax.axis('off')

# set the canvas size to be 8x6 inches


#
#
#
#
#

id_name = 'oracle'

if id_name in ['x', 'y', 'z', 'h', 'id', 's', 't', 'p', 'u']:
    fc = '#EE7057'
    label = id_name.capitalize()
elif id_name in ['rx', 'ry', 'rz']:
    fc = '#6366F1'
    label = id_name.upper()
elif id_name in ['oracle']:
    fc = '#8C9197'
    label = '?'
else:
    fc = 'white'
    label = ''


# create a FancyBboxPatch object
a = 0.5  # box width and height

DEEPCOLOR = '#0C161F'

color_dict = {'deep': DEEPCOLOR}


def add_label(text, x, y, fontsize):
    txt = ax.text(x, y, text,
                  fontsize=fontsize,
                  ha='center',
                  va='center',
                  color=DEEPCOLOR)
    # 添加白边效果
    txt.set_path_effects([pe.withStroke(linewidth=6, foreground='white')])
    return txt


_dy = -0.1 * a
txt = add_label(label, 0, _dy, fontsize=80)


bbox = FancyBboxPatch((-a / 2, -a / 2), a, a,
                      boxstyle=f'round, pad={0.2 * a}',
                      edgecolor=DEEPCOLOR,
                      facecolor=fc,
                      linewidth=3)
ax.add_patch(bbox)

# plt.savefig('figures/fancy_box.png', dpi=300, transparent=True)
plt.show()
