import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# x、y坐标数据读取和标签（需对应）
array = pd.read_excel('./N=200线性闭环三个二维图.xlsx').to_numpy()
labels = ['RC-DeePC', 'RS-DeePC', 'R-DeePC']

# 需保证长度相等
xs = array[:, 0]
ys_list = [array[:, i+1] for i in range(len(labels))]  # 列表

# 全局字体设置
plt.rc('font', family='Times New Roman')

# plt默认使用的颜色顺序
COLORS = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# 图片大小, 宽和高，单位为inch
plt.figure(figsize=(10, 5))

# 绘制曲线
for ys, name in zip(ys_list, labels):
    plt.plot(xs, ys, label=name)  # 可通过设置colors=COLORS[i]指定颜色

# 坐标轴范围
plt.xlim([np.min(xs), np.max(xs)])
# plt.ylim(<类似设置>)

# 对数尺标
plt.yscale('log')
plt.xscale('log')

# 图例
plt.legend(prop={'weight': 'normal', 'size': 20})

# 刻度
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

# 坐标标签
plt.xlabel(r'$\mu$', {'weight': 'normal', 'size': 20}, labelpad=-10.)
plt.ylabel('J', {'weight': 'normal', 'size': 24}, labelpad=-15.)

# 图边距
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.15)

# 标题
# plt.title('XXX')

# 保存/显示图片
# 备注：注意保存路径和格式后缀；dpi=digits per inch为像素值
plt.savefig('./linear_close_erweitu.eps', dpi=400)
plt.savefig('./linear_close_erweitu.png', dpi=400)
plt.show()
