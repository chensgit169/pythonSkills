import sympy as sp

# 定义变量和函数
x = sp.symbols('x')
f = x/(1+sp.sqrt(1-x))

# 在点x=0处进行二阶泰勒展开
order = 4
taylor_expansion = f.series(x, 0, order)  # .removeO()

print("Function:", f)
print("Taylor expansion up to order %d:" % order, taylor_expansion)
