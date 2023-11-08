import numpy as np
import matplotlib.pyplot as plt
import os

num = '200'
xs = np.load('coordinates/200.npy')
legends = ['R-DeepPC', 'RS-DeepPC', 'RC-DeepPC']
for i, name in enumerate(['分段', '因果关系', '非因果关系']):
    file_root = os.path.join('raw_data', num, '线性开环%s%s' % (num, name))
    data = np.load(os.path.join(file_root, 'j_descending.npy'))
    plt.plot(xs, data, label=legends[i])

plt.legend()

plt.xlabel(r'$\mu$')
plt.ylabel('$J$')
plt.yscale('log')
plt.xscale('log')
plt.savefig('%s.png' % num, dpi=400)
