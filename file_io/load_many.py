import os

data_dir = './0000/tensors/tensor_step1/URp_step1/'
directions = os.listdir(data_dir)
for d in directions:
    tensors = os.listdir(data_dir + f'{d}/')
    for t in tensors:
        t_name = t[:-4]
        print()
    print(tensors)
