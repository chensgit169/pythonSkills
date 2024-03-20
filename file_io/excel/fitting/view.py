import os
import xlwings as xw
import numpy as np
import matplotlib.pyplot as plt
# from scipy.optimize import least_squares
#
# file_dir = 'raw_data.xlsx'  # 表格文件名
# data_folder = 'extracted_data'  # 存放提取数据的文件夹
# image_folder = 'figures'  # 存放绘制的图像的文件夹
#
# # 创建文件夹
# os.makedirs(data_folder, exist_ok=True)
# os.makedirs(image_folder, exist_ok=True)
#
#
# # 从表格中提取数据并保存为更灵活的npy文件
def extract_data():
    with xw.Book(file_dir) as wb:  # 打开.xlsx文件
        sheet = wb.sheets['Sheet1']
        max_row_num = str(sheet.cells.last_cell.row)

        def read_col(col_name):
            """获取对应列的数据"""
            _data = sheet.range(col_name + '2:' + col_name + max_row_num).value
            return [_ for _ in _data if _ is not None]
#
#         xs = read_col("A")  # 横坐标
#         s = read_col("B")  # 因变量
#         x_beta = read_col("D")  # 增强因子的横坐标
#         beta = read_col("E")  # 增强因子
#
#         s1 = read_col("AA")  # 因变量
#         s2 = read_col("AB")  # 因变量
#         s3 = read_col("AC")  # 因变量
#         # 可以继续添加需要的列
#
#         # 保存
#         np.save(os.path.join(data_folder, 'xs.npy'), xs)
#         np.save(os.path.join(data_folder, 's.npy'), s)
#         np.save(os.path.join(data_folder, 'x_beta.npy'), x_beta)
#         np.save(os.path.join(data_folder, 'beta.npy'), beta)
#         np.save(os.path.join(data_folder, 's1.npy'), np.array(s1))
#         np.save(os.path.join(data_folder, 's2.npy'), np.array(s2))
#         np.save(os.path.join(data_folder, 's3.npy'),  np.array(s3))
#         # 可以继续添加需要的列
#
#
# # 从npy文件加载数据
# def load_data():
#     xs = np.load(os.path.join(data_folder, 'xs.npy'))
#     s = np.load(os.path.join(data_folder, 's.npy'))
#     x_beta = np.load(os.path.join(data_folder, 'x_beta.npy'))
#     beta = np.load(os.path.join(data_folder, 'beta.npy'))
#     s1 = np.load(os.path.join(data_folder, 's1.npy'))
#     s2 = np.load(os.path.join(data_folder, 's2.npy'))
#     s3 = np.load(os.path.join(data_folder, 's3.npy'))
#     return xs, s, x_beta, beta, s1, s2, s3
#
#
# # 可视化原始数据
# def visualize_raw_data():
#     """
#     可视化原始数据
#     """
#     xs, s, x_beta, beta, s1, s2, s3 = load_data()
#
#     # 可类似地绘制其他列的数据
#     plt.plot(x_beta, beta)  # 绘制数据点
#     plt.xlabel('x')  # 坐标轴标签
#     plt.ylabel(r'$\beta$')
#     plt.title('横坐标-增强因子', font='SimHei')  # 标题
#     plt.savefig(os.path.join(image_folder, '横坐标-增强因子-原始数据.png'), dpi=300)  # 保存图像
#
#
# # 要拟合的多元模型
# def model(params, s, beta):
#     """
#     要拟合的多元模型, A, C为拟合参数。S(λ)为初始值，β为增强因子。
#
#     即 A * S(λ) + C * β * S(λ), β * S(λ) = SE(λ)
#
#     拟合得到A, C后可得到B=1-A-C
#
#     Args:
#         params: A, C
#         s: S(λ)
#         beta: β
#     """
#     a, c = params
#     return a * s + c * beta * s
#
#
# # 误差函数
# def error(params, s, beta, si):
#     """
#     定义误差函数（残差函数）。
#     """
#     return model(params, s, beta) - si
#
#
# def fit_beta(vis: bool = False):
#     xs, s, x_beta, beta, s1, s2, s3 = load_data()
#     x, y = x_beta, beta
#
#     extra_lim = 570
#     linear_section = x < extra_lim
#     x_extra = x[linear_section]
#     y_extra = y[linear_section]
#
#     degree = 1  # 一次多项式外推
#     coefficients_extra = np.polyfit(np.array([430, 550]), np.array([400, 291.666]), degree)
#     xp_extra = np.linspace(430, 550, 200)
#     yp_extra = np.polyval(coefficients_extra, xp_extra)
#
#     degree = 7  # 多项式拟合
#     coefficients = np.polyfit(x, y, degree)
#     yp = np.polyval(coefficients, x)
#
#     def beta_func(xs_):
#         in_range = xs_ > np.min(x)
#         return np.polyval(coefficients_extra, xs_) * (1 - in_range) + np.polyval(coefficients, xs_) * in_range
#
#     if vis:
#         plt.plot(x, y, label='原始')
#         plt.plot(x, yp, label='%d阶多项式拟合' % degree)
#         plt.plot(xp_extra, yp_extra, label='线性外推')
#         # plt.plot([extra_lim, extra_lim], [0, 400], '--k')
#         # plt.text(extra_lim+1, 300, str(extra_lim), ha='left', va='bottom')
#
#         plt.xlabel('x')
#         plt.ylabel(r'$\beta$')
#         plt.legend(prop={'family': 'SimHei'})
#         plt.title('增强因子数据拟合', font='SimHei')
#         plt.savefig(os.path.join(image_folder, '增强因子数据拟合外推.png'), dpi=300)
#     return beta_func
#
#
# # 拟合提取A, B, C
# def fit_main():
#     xs, s, x_beta, _, s1, s2, s3 = load_data()
#
#     ax3 = plt.axes(projection='3d_plots')
#
#     in_range = xs > np.min(x_beta) - 1e7
#     xs = xs[in_range]
#     s = s[in_range]
#     i = 3
#     si = [s1, s2, s3][i-1]
#     s1 = si[in_range]
#
#     beta_func = fit_beta()
#     beta = beta_func(xs)
#     se = beta * s
#
#     result = fit(s, beta, s1)
#     s1_p = model(result['x'], s, beta)
#     fitted_params = result['x']
#     print("数据S%d," % i)
#     print("拟合值 A, C:", fitted_params[0], fitted_params[1])
#     print("B=1-A-C:", 1 - fitted_params[0] - fitted_params[1])
#     print("损失函数:", result['cost'])
#
#     ax3.scatter(s/1e5, se/1e5, s1/1e5, c='r', marker='o', label='原始')
#     ax3.scatter(s / 1e5, se / 1e5, s1_p / 1e5, c='b', marker='o', label='拟合')
#
#     ax3.set_xlabel(r'$S(\lambda)/10^5$')
#     ax3.set_ylabel(r'$SE(\lambda/10^5)$')
#     ax3.set_zlabel(r'$S1/10^5$')
#     plt.legend(prop={'family': 'SimHei'})
#     plt.title('Data S%d' % i)
#     plt.show()
#
#
# def fit(s, beta, si):
#     # 初始参数的猜测值
#     initial_params = (0.1, 0.5)
#
#     # 使用最小二乘法进行拟合
#     result = least_squares(error, initial_params, args=(s, beta, si))
#     return result
#
#
# if __name__ == '__main__':
#     # extract_data()
#     # fit_beta(vis=True)
#     # load_data()
#     fit_main()
#     # visualize_raw_data()
