# 导入相关包和方法
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares


# 定义要拟合的模型
def model(param, x):
    a, b = param
    return a * np.exp(b * x)


# 定义误差函数（残差函数），即观测值与模型预测值之间的差异
def error(params, x, y_observed):
    return model(params, x) - y_observed


# 生成含有随机噪声的虚拟数据
true_param = [1.0, -2.0]
xs = np.linspace(-1, 1, 30)
ys = model(true_param, xs) + 0.1 * np.random.rand(xs.shape[0])

# 初始参数的猜测值
initial_params = [0.5, 1.0]

# 使用 leastsq 进行拟合
result = least_squares(error, initial_params, args=(xs, ys), bounds=([0, 2]))

# 输出拟合得到的参数
fitted_params = result['x']
a, b = fitted_params
print("真实参数 (a, b):", true_param)
print("拟合参数 (a, b):", fitted_params)
print("损失函数（拟合误差的估计）：", result['cost'])

# 绘制数据和拟合
plt.plot(xs, ys, 'o', label='data')
plt.plot(xs, model(fitted_params, xs), label='$y=ae^{bx}$' + f'\na={a:.3f}, b={b:.3f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('fitting_bounded.png', dpi=300)  # 保存图片
