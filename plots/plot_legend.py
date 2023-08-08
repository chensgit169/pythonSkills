import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10, 1)
y = np.random.random(10)
plt.plot(x, y)
si = 's_x'
plt.text(0, 0, 'text\ntext', fontsize=15)
plt.title('$'+f'{si}' + '$')
plt.show()
