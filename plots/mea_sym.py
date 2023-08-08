import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import copy

plt.xkcd(randomness=300)

fig = plt.figure(figsize=(3, 3))
ax = fig.add_subplot(111, aspect='equal')
ax.axis('off')

box_cx = 0.25
box_cy = 0.25
box_width = 0.5

line_left = Line2D(xdata=(box_cx - box_width/2, box_cx),
                   ydata=(box_cx + box_width / 2, box_cx + box_width / 2),
                   linewidth=1.5, color='black')
ax.add_line(line_left)

line_right1 = Line2D(xdata=(box_cx + box_width, box_cx + 1.5 * box_width),
                     ydata=(box_cx + box_width / 2, box_cx + box_width / 2),
                     linewidth=1.5, color='black')
ax.add_line(line_right1)

line_right2 = Line2D(xdata=(box_cx + box_width, box_cx + 1.5 * box_width),
                     ydata=(0.9 * box_cx + box_width / 2, 0.9 * box_cx + box_width / 2),
                     linewidth=1.5, color='black')
ax.add_line(line_right2)


box = mpatches.Rectangle((box_cx, box_cy), width=box_width, height=box_width,
                         linewidth=1.5, fill=True, edgecolor='black')
ax.add_patch(box)

box2 = mpatches.Rectangle((box_cx + 1.5*box_width, box_cy), width=box_width, height=box_width,
                         linewidth=1.5, fill=True, edgecolor='black')

ax.add_patch(box2)

arc = mpatches.Arc((box_cx + box_width / 2, box_cy + 0.1 * box_width),
                   width=0.9 * box_width, height=0.9 * box_width,
                   linewidth=1.5, theta1=0, theta2=180, fill=False)
ax.add_patch(arc)

arrow = mpatches.Arrow(x=box_cx + box_width / 2, y=box_cy + 0.1 * box_width,
                       dx=0.1 * box_width, dy=0.8 * box_width, width=0.01,
                       linewidth=1.5, color='black', zorder=1)
ax.add_patch(arrow)

ax.set_xlim([0, 3])
ax.set_xlim([0, 3])

plt.title('measurement')
plt.tight_layout()

# plt.savefig('./measurement_cartoon.png', dpi=160)

plt.show()
