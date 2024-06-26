"""
===========================================================
Plot contour (level) curves in 3D using the extend3d option
===========================================================

This modification of the :doc:`contour3d` example uses ``extend3d=True`` to
extend the curves vertically into 'ribbons'.
"""

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

ax = plt.figure().add_subplot(projection='3d_plots')
X, Y, Z = axes3d.get_test_data(0.05)
ax.contour(X, Y, Z, extend3d=True, cmap=cm.coolwarm)

plt.show()
