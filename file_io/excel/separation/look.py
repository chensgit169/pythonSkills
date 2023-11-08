# coding: utf-8

import os
import xlwings as xw
import numpy as np
import matplotlib.pyplot as plt

app = xw.App(visible=False, add_book=False)

wb_200_0 = app.books.open('raw_data/200/线性开环200分段/线性开环200-cost-分段-list.xls')
wb_x = app.books.open('raw_data/坐标.xls')

ys = wb_200_0.sheets['Sheet1'].range('B2:B101').value
xs_200 = wb_x.sheets['Sheet1'].range('B2:B101').value
xs_400 = wb_x.sheets['Sheet1'].range('C2:C101').value
xs_600 = wb_x.sheets['Sheet1'].range('D2:D101').value
app.quit()

# np.save('raw_data/200/线性开环200-cost-分段-list.npy', ys)
np.save('coordinates/200.npy', xs_200)
np.save('coordinates/400.npy', xs_400)
np.save('coordinates/600.npy', xs_600)
# plt.plot(xs, ys)
plt.xlabel('$\mu$')
plt.ylabel('$J$')
plt.yscale('log')
plt.xscale('log')
# plt.show()
