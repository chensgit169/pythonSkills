import scipy.io as scio
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

dim = 100

keys = ['cost_rnonCausalDeePC_list', 'cost_rsegment_list', 'cost_hrsegment_list'][::-1]
renames = ['R-DeePC', 'RS-DeePC', 'RC-DeePC'][::-1]

num = '200'

raw_root = os.path.join('.\\raw_data', num, '数据20231101')
prod_root = os.path.join('.\\split_data', num, '数据20231101')
os.makedirs(prod_root, exist_ok=True)

data = scio.loadmat(os.path.join(prod_root, 'matlab.mat'))

print(data['RC-DeePC_descending_list'].tolist())
for k in data.keys():
    print(k)
