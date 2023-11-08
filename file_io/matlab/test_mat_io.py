import scipy.io as scio

data = scio.loadmat('test.mat')
array = data['test']
array[0, 0] = None
print(array)

# scio.savemat('test.mat', data)
