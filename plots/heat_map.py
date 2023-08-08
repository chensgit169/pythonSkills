import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# data = np.random.random((100, 100)) - 0.5
# fig = plt.figure()
# ax = fig.add_subplot(111)
#
# im = ax.imshow(data, cmap=cm.hot_r)
#
# plt.colorbar(im)
#
# plt.title("This is a title")
#
# plt.show()


data = np.array([[0, 1], [2, 3]])
plt.title('title')
plt.imshow(data, cmap='cool', interpolation='nearest')
plt.colorbar()
plt.xlabel('yes?')
plt.show()


