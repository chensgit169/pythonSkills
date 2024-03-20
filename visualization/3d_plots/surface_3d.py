import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np


fig = plt.figure()
ax3 = plt.axes(projection='3d_plots')

zs = np.linspace(-8, 8, 200)
rs = np.logspace(-4, -1, 103)

X, Y = np.meshgrid(zs, rs)
Z = np.sin(X) + np.cos(Y)

ax3.plot_surface(X, Y, Z, cmap='rainbow')
# ax3.contour(X, Y, Z, zdim='z', offset=-2, cmap='rainbow')
plt.show()
