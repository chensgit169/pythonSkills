import os

import matplotlib.pyplot as plt
import numpy as np

dim = 100

renames = ['R-DeePC', 'RS-DeePC', 'RC-DeePC'][::-1]


def main(num, dec: bool = True):
    prod_root = os.path.join('.\\split_files', num, '数据20231101')
    xs = np.load(os.path.join(prod_root, 'mu.npy'))

    plt.rc('font', family='Times New Roman')
    plt.figure(figsize=(10, 5))

    for i, name in enumerate(renames):
        descending_mean = np.load(os.path.join(prod_root, name + '_descending_mean.npy'))
        increasing_mean = np.load(os.path.join(prod_root, name + '_increasing_mean.npy'))
        if dec:
            plt.plot(xs, descending_mean, label=name)
        else:
            plt.plot(xs, increasing_mean, label=name)

    plt.xlim([np.min(xs), np.max(xs)])
    font = {'weight': 'normal', 'size': 20}
    plt.legend(prop=font)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel(r'$\mu$', {'weight': 'normal', 'size': 20}, labelpad=-10.)
    plt.ylabel('J', {'weight': 'normal', 'size': 24}, labelpad=-15.)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.15)
    plt.yscale('log')
    plt.xscale('log')

    # plt.title('Mean of $J$')
    # plt.show()
    # plt.tight_layout()
    if dec:
        file_name = '%s_%s' % (num, 'dec')
    else:
        file_name = '%s_%s' % (num, 'inc')
    plt.savefig(os.path.join(prod_root, file_name + '.eps'), dpi=400)
    plt.savefig(os.path.join(prod_root, file_name + '.png'), dpi=400)


if __name__ == '__main__':
    for num in ['200']:
        main(num, dec=False)
