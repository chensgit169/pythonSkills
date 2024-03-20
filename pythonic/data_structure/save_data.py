import numpy as np

a = np.random.random(1)
b = np.random.random((1, 2))
data = {'a': a, 'b': b}
np.savez('data.npz', **data)

data = np.load('data.npz')
print(type(data))
print(type(data['a']))
