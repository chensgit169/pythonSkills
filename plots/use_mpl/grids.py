import matplotlib.pyplot as plt
import numpy as np

# overall size of circuit
depth = 20
bit_num = 10
xs = np.arange(0, depth+1)
ys = np.arange(0, bit_num+1)

fig = plt.figure()
_size_x = 0.48 * (depth+2)
_size_y = 0.48 * (bit_num+2)
fig.set_size_inches(_size_x, _size_y)
fig.set_dpi(100.0)

ax = fig.add_subplot(111, aspect='equal')

ax.set_xlim(-1, depth+1)
ax.set_ylim(-1, bit_num+1)

x, y = np.meshgrid(xs, ys)
plt.title('Test', fontsize=20)
ax.plot(x, y, 'o', color='black')
if depth/bit_num >= 2 or bit_num/depth >= 2:
    fig.tight_layout()

# plt.show()
plt.savefig('figures/test.png', dpi=300)
