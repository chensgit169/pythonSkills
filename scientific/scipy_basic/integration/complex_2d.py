import numpy as np
from scipy.integrate import dblquad


# 2025年7月20日验证半经典Rabi模型Magnus展开第二项

# 被积函数
def integrand(x, y):
    return np.sin(np.cos(x) - np.cos(y))

# 外层积分变量 y ∈ [0, 2π]
# 内层积分变量 x ∈ [0, y]
result, error = dblquad(
    func=integrand,
    a=0,
    b=2*np.pi,
    gfun=lambda y: 0,
    hfun=lambda y: y
)

print("积分结果:", result)
print("估计误差:", error)
