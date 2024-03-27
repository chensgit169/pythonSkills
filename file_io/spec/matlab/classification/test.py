import scipy.io as scio
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

dim = 100

keys = ['cost_rnonCausalDeePC_list', 'cost_rsegment_list', 'cost_hrsegment_list'][::-1]
renames = ['R-DeePC', 'RS-DeePC', 'RC-DeePC'][::-1]


def is_descending(data_: np.ndarray):
    assert data_.shape == (dim,), f'{data_.shape}'

    diff = data_[1:] - data_[:-1]
    descending = diff <= 1e-15
    # print(np.mean(descending))

    # 判据（均有效）
    # criterion = np.all(descending)
    # criterion = not (np.min(raw_data) < raw_data[-1])  # 一直减少的判据（可选）
    criterion = np.mean(descending) > 0.99  # 一直减少的判据：下降频率高于99%认为是一直减少
    return criterion


def main(num, save: bool = False):
    raw_root = os.path.join('.\\raw_data', num, '数据20231101')
    prod_root = os.path.join('.\\split_files', num, '数据20231101')
    os.makedirs(prod_root, exist_ok=True)

    data = scio.loadmat(os.path.join(raw_root, 'matlab.mat'))
    xs = data['mulist'].reshape(-1)
    np.save(os.path.join(prod_root, 'mu.npy'), xs)

    arrays = [data[key] for key in keys]  # type: list[np.ndarray]
    data_ = {}
    for i, array in enumerate(arrays):
        name = renames[i]

        idx = np.ones(dim, dtype=bool)
        array_descending = array.copy()
        array_increasing = array.copy()
        for i in range(dim):
            _descend = is_descending(array[:, i])
            idx[i] = _descend
            if _descend:
                array_increasing[:, i] = np.nan
            else:
                array_descending[:, i] = np.nan

        data_[name + '_descending_list'] = array_descending.tolist()
        data_[name + '_increasing_list'] = array_increasing.tolist()

        df = pd.DataFrame(array_descending)
        print(os.path.join(prod_root, name + '_descending_list'+'.xlsx'))
        df.to_excel(os.path.join(prod_root, name + '_descending_list'+'.xlsx'), sheet_name='Sheet1', index=True)

        df = pd.DataFrame(array_increasing)
        df.to_excel(os.path.join(prod_root, name + '_increasing_list' + '.xlsx'), sheet_name='Sheet1', index=True)

        descending_mean = np.mean((array.T[idx]).T, axis=1)
        increasing_mean = np.mean((array.T[~idx]).T, axis=1)

        df = pd.DataFrame(descending_mean)
        df.to_excel(os.path.join(prod_root, name + '_descending_mean' + '.xlsx'), sheet_name='Sheet1', index=True)
        df = pd.DataFrame(increasing_mean)
        df.to_excel(os.path.join(prod_root, name + '_increasing_mean' + '.xlsx'), sheet_name='Sheet1', index=True)

        data_[name + '_descending_mean'] = descending_mean.tolist()
        data_[name + '_increasing_mean'] = increasing_mean.tolist()
        np.save(os.path.join(prod_root, name + '_descending_mean.npy'), descending_mean)
        np.save(os.path.join(prod_root, name + '_increasing_mean.npy'), increasing_mean)

        # descending_array = (array.T[~idx]).T
        # print(descending_array.shape)
        # plt.plot(xs.reshape(-1), np.mean(descending_array, axis=1), label=name)

        print('%s, %s, "一直下降"的数目:' % (num, name), np.sum(idx))

        # 保存数据
        if save:
            df = pd.DataFrame(array)
            xlsx_path = os.path.join(prod_root, name + '.xlsx')
            df.to_excel(xlsx_path, sheet_name='Sheet1', index=True)

    scio.savemat(os.path.join(prod_root, 'matlab.mat'), data_)
    # plt.legend()
    #
    # plt.xlim([np.min(xs), np.max(xs)])
    # plt.xlabel(r'$\mu$')
    # plt.ylabel('$J$')
    # plt.yscale('log')
    # plt.xscale('log')
    # plt.show()
    # plt.savefig(os.path.join(prod_root, '%s.eps' % num), dpi=400)
    # plt.savefig(os.path.join(prod_root, '%s.eps' % num), dpi=400)



if __name__ == '__main__':

    for num in ['200', '400', '600']:
        print('///////////////////////////////////////////')
        main(num)
