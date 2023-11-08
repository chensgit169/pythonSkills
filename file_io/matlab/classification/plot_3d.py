import scipy.io as scio
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

dim = 100

keys = ['cost_rnonCausalDeePC_list', 'cost_rsegment_list', 'cost_hrsegment_list'][::-1]
renames = ['R-DeePC', 'RS-DeePC', 'RC-DeePC'][::-1]


def main(num):
    raw_root = os.path.join('.\\raw_data', num, '数据20231101')
    prod_root = os.path.join('.\\prod_data', num, '数据20231101')
    os.makedirs(prod_root, exist_ok=True)

    data = scio.loadmat(os.path.join(raw_root, 'matlab.mat'))
    xs = data['mulist'].reshape(-1)

    array = [data[key] for key in keys][2]   # type: list[np.ndarray]
    order = array[0].argsort()
    array = array.T[order].T

    ax3 = plt.axes(projection='3d')
    # X, Y = np.meshgrid(range(dim), range(dim))
    X, Y = np.meshgrid(np.log(xs), np.log(xs))
    ax3.plot_surface(X, Y, array.T, cmap='rainbow')

    scio.savemat('../test.mat', {'test': array})
    # ax3.plot_wireframe(X, Y, array, color='k')

    # ax3.set_xticks([1e-10, 1e-5, 0, 1e5, 1e10])
    # ax3.set_yticks([1e-10, 1e-5, 0, 1e5, 1e10])
    # ax3.set_xticklabels(xs.astype(np.int32))
    # ax3.set_yticklabels(xs.astype(np.int32))
    ax3.set_xticks([-10, -5, 0, 5, 10])  # 设置刻度
    ax3.set_xticklabels(['$10^{-10}$', '$10^{-5}$', '$0$', '$10^{5}$', '$10^{10}$'])  # 设置刻度标签

    ax3.set_yticks([-10, -5, 0, 5, 10])  # 设置刻度
    ax3.set_yticklabels(['$10^{-10}$', '$10^{-5}$', '$0$', '$10^{5}$', '$10^{10}$'])  # 设置刻度标签

    ax3.set_xlabel(r'$\mu$')
    ax3.set_zlabel(r'$J$')
    ax3.set_ylabel(r'$\lambda$')
    # ax3.set_xscale('log')
    # ax3.set_yscale('log')
    # ax3.set_zscale('log')

    plt.title('RC-DeePC')
    plt.show()


if __name__ == '__main__':

    for num in ['200', '400', '600'][:1]:
        print('///////////////////////////////////////////')
        main(num)
