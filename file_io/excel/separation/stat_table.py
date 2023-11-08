# coding: utf-8

import os
import xlwings as xw
import numpy as np
import matplotlib.pyplot as plt

# app = xw.App(visible=False, add_book=False)  # visible=True   显示Excel工作簿；False  不显示工作簿


def main(name, num):
    file_root = os.path.join('raw_data', num, '线性开环%s%s' % (num, name))

    with open(os.path.join(file_root, '统计.txt'), 'r', encoding='utf-8') as f:
        n_1 = f.readline().strip().split('：')[1]
        n_2 = f.readline().strip().split('：')[1]
        n_1, n_2 = int(n_1), int(n_2)
        print(name, num, n_1, n_2)


if __name__ == '__main__':
    for num in ['200', '400', '600']:
        for name in ['分段', '因果关系', '非因果关系']:
            main(name, num)
