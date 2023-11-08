#!/usr/bin/env python
# encoding: gbk
# -*- coding:utf-8 -*-


import matplotlib.pyplot as plt
import pandas as pd

file = r"C:\Users\XITer\Desktop\15-30-200非线性开环无噪声 - 转置.xls"
# file=r"F:\personal\others-M\23.10.12python\15-30-200非线性开环无噪声.xls"
data = pd.read_excel(file)
data1 = data.query("Type == 'C-SPC'").to_numpy()
data2 = data.query("Type == 'S-SPC'").to_numpy()
data3 = data.query("Type == 'SPC'").to_numpy()

x1, x2, x3 = data1[:, 1], data2[:, 1], data3[:, 1]
y1, y2, y3 = data1[:, 2], data2[:, 2], data3[:, 2]

plt.plot(x1, y1, x2, y2, x3, y3, linestyle='-', marker='o', markersize=8)
# f=sbn.boxplot(x=data['epsilon'],y=data['J'],data=data,\
#            hue=data['Type'],width=0.8,showbox=0)


plt.grid(True, alpha=0.5)

plt.rc('font', family='Times New Roman')
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
# plt.xlim(0,1000)
# plt.ylim(0,30)
# front是标签属性：包括字体、大小等
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 30,
        }
plt.xlabel("ε", font)
plt.ylabel("J", font)
plt.rcParams.update({'font.size': 30})
plt.legend(['C-SPC', 'S-SPC', 'SPC'], loc='upper left')

# plt.figure(figsize=(8,6)) #图像大小

plt.show()
