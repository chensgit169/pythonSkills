import numpy as np
from scipy.optimize import least_squares

true_param = [1.0, 2.0, 3.0, 4.0]


# 定义要拟合的多元线性模型
def model(params, x1, x2, x3):
    a, b, c, d = params
    return a * x1 + b * x2 + c * x3 + d


# 定义误差函数（残差函数），即观测值与模型预测值之间的差异
def error(params, x1, x2, x3, y_observed):
    error_ = model(params, x1, x2, x3) - y_observed
    return error_


# 生成虚拟数据，注意：自变量之间不能有太强的相关性
x1 = np.random.randn(100) * 2.0 - 3
x2 = np.random.randn(100) * 0.5 + 1
x3 = np.random.randn(100) * 1.5 + 2
y_observed = model(true_param, x1, x2, x3)

# 初始参数的猜测值
initial_params = [1.0, 1.0, 1.0, 1.0]

# 使用 leastsq 进行拟合
result = least_squares(error, initial_params, args=(x1, x2, x3, y_observed))
fitted_params = result['x']

# 输出拟合得到的参数
print("拟合参数 (a, b, c, d):", fitted_params)
print(np.sum(np.abs(y_observed - model(fitted_params, x1, x2, x3))**2))
print("损失函数（拟合误差的估计）：", result['cost'])
