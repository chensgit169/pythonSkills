import numpy as np
import matplotlib.pyplot as plt

xs = np.linspace(-10, 10, 100)
ys = np.arctan(xs)
plt.plot(xs, ys)
plt.show()
