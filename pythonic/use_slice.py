import numpy as np

a = np.random

order = 5
lower = [1, 2, 1, 2, 0]
upper = [7, 4, 6, 5, 6]
slices = [slice(lower[i], upper[i]) for i in range(5)]
